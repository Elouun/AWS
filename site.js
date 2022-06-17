const http = require("http");
const fs = require('fs');
const fsp = require('fs').promises;

const host = '192.168.1.60';
//const host = 'localhost';

const port = 8000;
const axios = require('axios');

const { exec } = require("child_process");



let indexFile;
let pageHtml;


let marker = " new google.maps.Marker({ position: new google.maps.LatLng($lat, $lng),    map: map,    icon:{  url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'  },  label: {text: ' $text ', color: 'white'} });" ;


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

		    //console.log(`stdout: ${stdout}`);
		    resolve(stdout);
		    
		});
	});
}


const requestListener = async function (req, res) {   
	if (req.url != "/favicon.ico" && req.url != "/index.js"){
		let param = "";
		console.log("requete du site:")
		console.log(req.url.replace(/[?].*/gi, ''));
		indexFile=pageHtml;

		switch (req.url.replace(/[?].*/gi, '')) {


			case "/serve":
				if (req.url.split('resto=')[1] === undefined) {
					res.writeHead(404);
					res.end("Missing param ");	
				}
				else {
					param = req.url.split('resto=')[1].replace(/\+/gi, ' ');
					console.log(param);
					request_aws("https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getRestaurant/" +param ,res)
				}
			    break;

			case "/recommandation_french": 
				if (req.url.split('reco=')[1] === undefined) {
					res.writeHead(404);
					res.end("Missing param ");	
				}
				else {
					param = req.url.split('reco=')[1].replace(/%2C/gi, ',');
					console.log(param);
					let result_reco = await commande_aws("python3 ./model/testModelFrench.py " + param + " 2> err.log");


					res.setHeader("Content-Type", "application/json");
					res.writeHead(200);
					res.end(result_reco);
				}
				break;

				
			
			case "/recommandation_indian":
				if (req.url.split('reco=')[1] === undefined) {
					res.writeHead(404);
					res.end("Missing param ");	
				}
				else {
					param = req.url.split('reco=')[1].replace(/%2C/gi, ',');
					console.log(param);
					let result_reco_indian = await commande_aws("python3 ./model/testModelIndian.py " + param + " 2> err.log");
				
				
					res.setHeader("Content-Type", "application/json");
					res.writeHead(200);
					res.end(result_reco_indian);
				}
				break;
			

			case "/image": 
				param = req.url.split('img=')[1];
				if(param === undefined ){
					res.writeHead(404);
				}
				else {
					var path = "/home/pi/Pictures/processed/" + param;  
					console.log(path);
					res.writeHead(200, {
					  'Content-Type' : 'image/png'
					});
					fs.createReadStream(path)
						.on('error', function(){   
							console.log("err image");
							res.writeHead(404);
							res.end("Image not found " + path);

						})
						.pipe(res).on('error', onError);

				}	
				break;	    		

			case "/recommandation_comparaison": 
				
				let result_French = await commande_aws("curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getCategoriesOr/French,Indian,usr_50854_french --silent");
				let result_Indian = await commande_aws("curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getCategoriesOr/French,Indian,usr_50854_indian --silent");



				result_French = JSON.parse(result_French);
				result_Indian = JSON.parse(result_Indian);

				console.log(result_French);

				console.log(result_Indian);

				console.log(result_French.length);


				/*
				
				let result_Marker_html = "";
				for (let i = 0 ; i < result_dataReco.length ; i++){


					result_Marker_html = result_Marker_html + "   " + marker
												.replace(/\$text/,result_dataReco[i][6])
											   	.replace(/\$lat/,result_dataReco[i][2])
											   	.replace(/\$lng/,result_dataReco[i][3])
				}
				console.log(result_Marker_html);


				indexFile = indexFile.toString().replace( /\/\/CHECKPOINT_1/, result_Marker_html)
				
				*/
				

			case "/":
				const cmd_url = "cd /home/pi/AWS/serveur_aws && chalice url"
				let result_url_cmd = await commande_aws(cmd_url);
				result_url_cmd = result_url_cmd.replace(/\n/ig,"<br>");
				indexFile = indexFile.toString().replace(/%%CMD_1_NAME%%/i ,"chalice url" );
				indexFile = indexFile.toString().replace(/%%CMD_1_RES%%/i ,result_url_cmd );
				
				const cmd_stat = "curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getStatistiques/ --silent"
				let result_stat_cmd = await commande_aws(cmd_stat);
				result_stat_cmd = JSON.parse(result_stat_cmd);


				indexFile = indexFile.toString().replace(/%%CMD_STAT_1_RES%%/i ,result_stat_cmd[0] );
				indexFile = indexFile.toString().replace(/%%CMD_STAT_2_RES%%/i ,result_stat_cmd[1] );
				indexFile = indexFile.toString().replace(/%%CMD_STAT_3_RES%%/i ,parseInt(result_stat_cmd[2])+4);


				const cmd_tps = "bash /home/pi/AWS/temps_traitement.sh 2>&1"
				let result_tps_cmd = await commande_aws(cmd_tps);
				result_tps_cmd = result_tps_cmd.replace(/[\n]+/ig,"<br>").replace(/\t/ig," ").split(';;');

				indexFile = indexFile.toString().replace(/%%CMD_TPS_1_RES%%/i ,result_tps_cmd[0] );
				indexFile = indexFile.toString().replace(/%%CMD_TPS_2_RES%%/i ,result_tps_cmd[1] );
				indexFile = indexFile.toString().replace(/%%CMD_TPS_3_RES%%/i ,result_tps_cmd[2] );


				res.setHeader("Content-Type", "text/html");
				res.writeHead(200);


				res.end(indexFile);
				break;
		};
	}

}

const server = http.createServer(requestListener);

fsp.readFile(__dirname + "/page.html")
    .then(contents => {
        pageHtml = contents;
        server.listen(port, host, () => {
            console.log(`Server is running on http://${host}:${port}`);
        });
    })
    .catch(err => {
        console.error(`Could not read index.html file: ${err}`);
        process.exit(1);
    });



