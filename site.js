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


let marker = " new google.maps.Marker({ position: new google.maps.LatLng($lat, $lng),    map: map,    icon:{  url: 'http://maps.google.com/mapfiles/ms/icons/$color-dot.png'  },  label: {text: ' $text ', color: 'white'} });" ;


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


				let result_Marker_html = "";
				let result_Table_html ="<table>  <thead> <tr>  <th colspan='2'>Tableau de  comparaison</th>  </tr>  </thead><tbody>  <tr>  <td>Indian</td>   <td>French</td>  </tr>";

				Object.keys(result_French).forEach(function(key) {
  					result_Marker_html = result_Marker_html + "   " + marker
												.replace(/\$text/,result_French[key]['id_new'])
												.replace(/\$color/,'green')
											   	.replace(/\$lat/,result_French[key]['latitude'])
											   	.replace(/\$lng/,result_French[key]['longitude']);
				
				});

				Object.keys(result_Indian).forEach(function(key) {
  			  		result_Marker_html = result_Marker_html + "   " + marker
												.replace(/\$text/,result_Indian[key]['id_new'])
												.replace(/\$color/,'blue')
											   	.replace(/\$lat/,result_Indian[key]['latitude'])
											   	.replace(/\$lng/,result_Indian[key]['longitude']);
				
				});


				Object.keys(result_Indian).forEach(function(key) {
					colorFrench ="neutre"
					colorIndian ="neutre"

					if (result_Indian[key]["categories"].includes("Indian")){
						if (result_Indian[key]["categories"].includes("French")){
							colorIndian="green"
						}
						else {
							colorIndian="yellow"
						}

					}
					if (result_French[key]["categories"].includes("French")){
						if (result_French[key]["categories"].includes("Indian")){
							colorFrench="green"
						}
						else {
							colorFrench="red"
						}

					}

  			  		result_Table_html = result_Table_html + "<tr> <td class='"+colorIndian+"'>"+result_Indian[key]["name"]+"</td> <td class='"+colorFrench+"'>"+result_French[key]["name"]+"</td> </tr>"
												
				
				})


				indexFile = indexFile.toString().replace( /\/\/CHECKPOINT_1/, result_Marker_html)
				indexFile = indexFile.toString().replace( /<!--CHECKPOINT_2-->/, result_Table_html + "</tbody> </table>")


	

			case "/":
				if (req.url.replace(/[?].*/gi, '') != "/recommandation_comparaison" ) {
					console.log("all resto");
					let result_all = await commande_aws("curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getLoca/ --silent");
					result_all = JSON.parse(result_all);
					marker_all = "";
					for (let i=0 ; i < result_all.length ; i++){
						marker_all = marker_all + "   " + marker
												.replace(/\$text/,result_all[i][0])
												.replace(/\$color/,'red')
											   	.replace(/\$lat/,result_all[i][1])
											   	.replace(/\$lng/,result_all[i][2]);

					}

					indexFile = indexFile.toString().replace( /\/\/CHECKPOINT_1/, marker_all)



				}
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



