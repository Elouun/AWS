const http = require("http");
const fs = require('fs').promises;

const host = 'localhost';
const port = 8000;
const axios = require('axios');

const { exec } = require("child_process");



let indexFile;


function request_aws(url,res) {
	axios.get(url)
  	.then(response => {
 	 	console.log(response.data);
 	 	res.writeHead(200);
        res.end(response.data);
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
	console.log(req.url);

	 switch (req.url) {
        case "/serve":
        	request_aws("https://www.google.fr/",res)

            break
        case "/":
        	let result_cmd = await commande_aws("ls -la");
        	result_cmd = result_cmd.replace(/\n/ig,"<br>");
            res.setHeader("Content-Type", "text/html");
    		res.writeHead(200);
    		indexFile = indexFile.toString().replace(/%%CMD_1%%/i ,result_cmd );
    		 console.log(indexFile);

    		res.end(indexFile);
    		break;
	};

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



