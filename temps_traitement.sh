echo "user:"
time curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getUserid/-_2h2cJlBOWAYrfplMU-Cg --silent > /dev/null 2> /dev/null
echo "restaurant:"
time curl "https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getCloserRestaurant?lat=39.93450004198443&long=-75.19926226811313 --silent > /dev/null"
echo "model:"
time python3 ./model/testModel.py 1,2,3,4,5,6,7,8,9,10_1,1,1,1,1,1,1,1,1,1 2> err.log > /dev/null
