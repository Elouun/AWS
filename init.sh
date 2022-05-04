
ORANGE='\e[0;33m'
NC='\e[0;m' 


echo_cmd(){
	echo -e "${ORANGE}$1${NC}"
}


echo_cmd "\napt get install"
echo_cmd "\n\tcurl"
sudo apt install curl 
echo_cmd "\n\tawscli"
sudo apt install awscli 

echo_cmd "\nget nvm cmd"
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
export NVM_DIR=$HOME/.nvm;
source $NVM_DIR/nvm.sh;

echo_cmd "\naws install"
cd serveur_aws
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
unzip awscliv2.zip
sudo ./aws/install


echo_cmd "\npip install"
echo_cmd "\n\thttpie"
pip install httpie
echo_cmd "\n\tchalice"
pip install chalice
echo_cmd "\n\tpymysql"
pip install pymysql
echo_cmd "\n\nnvm use"
nvm use

echo_cmd "\n configuration aws"
aws configure



echo_cmd "aws ec2 describe-regions"
echo_cmd "chalice deploy"
