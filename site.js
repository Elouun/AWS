const http = require("http");
const fs = require('fs');
const fsp = require('fs').promises;

const host = '192.168.1.60';
//const host = 'localhost';

const port = 8000;
const axios = require('axios');

const { exec } = require("child_process");



let indexFile;


function onError(err) {
  // `this` === stream that encountered the error
  console.log(err);
}

function request_aws(url,res) {
	axios.get(url)
  	.then(response => {
 	 	console.log(response.data);
		res.setHeader("Content-Type", "application/json");
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
		    }

		    console.log(`stdout: ${stdout}`);
		    resolve(stdout);
		    
		});
	});
}


const requestListener = async function (req, res) {   
	if (req.url != "/favicon.ico"){
		let param = "";
		
		console.log(req.url.replace(/[?].*/gi, ''));

		switch (req.url.replace(/[?].*/gi, '')) {


			case "/serve":
				param = req.url.split('resto=')[1].replace(/\+/gi, ' ');
				console.log(param);
				request_aws("https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getRestaurant/" +param ,res)
			    break;

			case "/recommandation": 
				param = req.url.split('reco=')[1].replace(/%2C/gi, ',');
				console.log(param);
				let result_reco = await commande_aws("python3 ./model/testModel.py " + param + " 2> err.log");
		    		
				
				res.setHeader("Content-Type", "application/json");
				res.writeHead(200);
				res.end(result_reco);
				break;

			case "/image": 
				param = req.url.split('img=')[1];
				if(param === undefined ){
					res.writeHead(404);
				}
				else {
					var path = "/home/pi/Pictures/" + param;  
					console.log(path);
					res.writeHead(200, {
					  'Content-Type' : 'image/png'
					});
					fs.createReadStream(path)
						.on('error', function(){   
							console.log("err image");
						})
						.pipe(res).on('error', onError);

				}	
				break;	    		


			case "/":
				const cmd_url = "cd /home/pi/AWS/serveur_aws && chalice url"
				let result_url_cmd = await commande_aws(cmd_url);
				result_url_cmd = result_url_cmd.replace(/\n/ig,"<br>");
				indexFile = indexFile.toString().replace(/%%CMD_1_NAME%%/i ,"chalice url" );
				indexFile = indexFile.toString().replace(/%%CMD_1_RES%%/i ,result_url_cmd );
				
				const cmd_stat = "curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getStatistiques/"
				let result_stat_cmd = await commande_aws(cmd_stat);
				console.log("toto");
				console.log(result_stat_cmd);
				console.log("end");
				result_stat_cmd = JSON.parse(result_stat_cmd);
				console.log(result_stat_cmd)

				
				indexFile = indexFile.toString().replace(/%%CMD_STAT_1_RES%%/i ,result_stat_cmd[0] );
				indexFile = indexFile.toString().replace(/%%CMD_STAT_2_RES%%/i ,result_stat_cmd[1] );
				indexFile = indexFile.toString().replace(/%%CMD_STAT_3_RES%%/i ,result_stat_cmd[2] );


				res.setHeader("Content-Type", "text/html");
				res.writeHead(200);

				console.log(indexFile);

				res.end(indexFile);
				break;
		};
	}

}

const server = http.createServer(requestListener);

fsp.readFile(__dirname + "/page.html")
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



