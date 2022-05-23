const http = require("http");
const fs = require('fs').promises;

const host = '192.168.1.60';
//const host = 'localhost';

const port = 8000;
const axios = require('axios');

const { exec } = require("child_process");



let indexFile;


function request_aws(url,res) {
	axios.get(url)
  	.then(response => {
 	 	console.log(response.data);
 	 	res.writeHead(200);
        	res.end(JSON.stringify(response.data));
  	})
 	.catch(error => {
   		console.log(error);
  	});
}
function commande_aws(cmd){
	return new Promise(resolve => {
		exec(cmd, (error, stdout, stderr) => {
		    if (error) {
		        console.log(`error: ${error.message}`);
		    	resolve(error.message);
		    }
		    if (stderr) {
		        console.log(`stderr: ${stderr}`);
		    	resolve(stderr);
		    }
		    console.log(`stdout: ${stdout}`);
		    resolve(stdout);
		});
	});
}


const requestListener = async function (req, res) {   
	if (req.url != "/favicon.ico"){
		console.log(req);

		console.log(req.url);
		console.log(req.url.replace(/[?].*/gi, ''));

		switch (req.url.replace(/[?].*/gi, '')) {


			case "/serve":
				request_aws("https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getRestaurant/Sister Honeys",res)
			    	break;


				// need to look like
				// http://localhost:8000/recommandation?value=value_that_you_need_for_your_model
			case "/recommandation": 
				console.log("reco");
				let param = req.url.split('value=')[1];
				let result_reco = await commande_aws("python3 ./model/testModel.py " + param + " 2> err.log");
		    		res.setHeader("Content-Type", "application/json");
				res.writeHead(200);
				res.end(result_reco);
				break;


			case "/":
				const cmd = "cd /home/pi/AWS/serveur_aws && chalice url"
				let result_cmd = await commande_aws(cmd);
				result_cmd = result_cmd.replace(/\n/ig,"<br>");
				res.setHeader("Content-Type", "text/html");
				res.writeHead(200);
				indexFile = indexFile.toString().replace(/%%CMD_1_NAME%%/i ,cmd );
				indexFile = indexFile.toString().replace(/%%CMD_1_RES%%/i ,result_cmd );
				console.log(indexFile);

				res.end(indexFile);
				break;
		};
	}

}

const server = http.createServer(requestListener);

fs.readFile(__dirname + "/page.html")
    .then(contents => {
        indexFile = contents;
        server.listen(port, host, () => {
            console.log(`Server is running on http://${host}:${port}`);
        });
    })
    .catch(err => {
        console.error(`Could not read index.html file: ${err}`);
        process.exit(1);
    });



