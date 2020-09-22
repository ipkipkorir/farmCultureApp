from flask import Flask, request
import africastalking
import os

app = Flask(__name__)

username = "sandbox"
api_key = "3c5ec2b526947ba76429feb18740bb3146e94ad543c0d76041c5faa9d1359db7"

africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods = ['POST', 'GET'] )
def ussd_callback():
	global response
	session_id = request.values.get("sessionId", None)
	service_code = request.values.get("serviceCode", None)
	phone_number = request.values.get("phoneNumber", None)
	text = request.values.get("text", "default")
	sms_phone_number = []
	sms_phone_number.append(phone_number)


	#USSD logic
	if text == "" or text == "111":
		#print main menu
		response = "CON Welcome to FarmCulture!\n"
		response += "LEARN & PRACTICE PROFESSIONAL FARMING\n"
		response += "1. GET STARTED\n"
		response += "000. EXIT\n"

	elif text == "1":
		#print menu for option 1
		response = "CON What would you like to LEARN?\n"
		response += "1. Horticultural farming\n"
		response += "2. Dairy Farming\n"
		response += "3. Beef Farming\n"
		response += "4. Poultry Farming\n"
		response += "5. Bee keeping\n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"

	elif text == "000": 
		#print menu for option 2
		response = "END Thank you and Goodbye. See you soon.\n"
		

	elif text == "1*1": 
		#print menu for horticulture option
		response = "CON LEARN HORTICULTURE:\n"
		response += "1. How to cultivate Groundnuts\n"
		response += "2. How to cultivate Maize\n"
		response += "3. How to cultivate Wheat\n"
		response += "4. How to cultivate Tomatoes\n"
		response += "5. How to cultivate Kales/Sukuma Wiki\n"
		response += "6. How to cultivate Green Grams\n"
		response += "7. How to cultivate Cabbage\n"
		response += "8. How to cultivate Spinach\n"
		response += "9. How to cultivate Macademia nuts\n"
		response += "10. How to cultivate Purple Tea\n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"

	elif text == "1*2":
		#print menu for dairy farming option
		response = "CON LEARN DAIRY FARMING:\n"
		response += "1. How to Dairy Cow Farming\n"
		response += "2. How to Dairy Goat Farming\n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"
			
	elif text == "1*3":
		#print menu option for beef farming 
		response = "CON LEARN BEEF FARMING:\n"
		response += " .... ... .. . \n"
		response += "000. EXIT\n"

	elif text == "1*4":
		#print menu for poultry farming
		response = "CON LEARN POULTRY FARMING:\n"
		response += "1. How to Layers Farming \n"
		response += "2. How to Broiler Farming \n"
		response += "111. Go Back\n"
		response += "000. EXIT\n"

	elif text == "1*5":
		#print menu for bee keeping
		response = "CON LEARN BEE KEEPING:\n"
		response += " .... ... .. . \n"
		response += "000. EXIT\n"

	elif text == "1*1*1":
		#send an SMS to user and print success message
		response = "CON GROUNDNUT FARMING:\n"
		response += "CLIMATE CONDITIONS:\n"
		response += "Altitude: Below 1500m above sea level.\n"
		response += "Temperature: 28-30 decrees celcius.\n"
		response += "Rainfall: 500-600mm well-distributed.\n"
		response += "Soil: Well-drained soil.\n"
		response += "Soil pH: Acidic soil of 6.0pH-6.5pH\n"
		response += "SOME OF THE VARIETIES:\n"
		response += "Red Oriata, Manipinta,Makulu Red, Bukene, \n"
		response += "Homa Bay, Texas Peanut, Red Valencia, Atika.\n"
		response += "HOW TO PLANT:\n"
		response += "Spacing between rows:\n"
		response += " 30cm - 45cm depending on variety.\n"
		response += "Spacing between plants:\n"
		response += " 15cm - 20cm depending on variety.\n"
		response += "Sowing depth: 5cm - 6cm deep.\n"
		response += "About 16kgs of seeds per acre.\n"
		response += "WEEDING:\n"
		response += "Start weeding 2-3weeks after germination.\n"
		response += "Weed often during the early stages of growth.\n"
		response += "Earthle up during weeding to ecourage pegging or \n"
		response += " penetration of nuts into to the soil.\n"
		response += "Use hand weeding after the start of pegging \n"
		response += "to avoid disturbing the growing nuts\n"
		response += "or damaging the flowers.\n"
		response += "Do clean weeding up to 6 weeks, \n"
		response += " then perform only hand weeding.\n"
		response += "FERTILIZER:\n"
		response += "Use adequate Calcuim when pods are forming.\n"
		response += "Use phosphate at the rate of 40kgs per acre\n"
		response += " to boost the firmness of the crop.\n"
		response += "DESEASE AND PEST CONTROL:\n"
		response += "Some of the deseases: \n"
		response += " Rust, Bacteria Wilt, Groundnut Rosette virus,\n "
		response += " leaf spot, crown rot and damping off disease.\n"
		response += "Some of the pests: \n"
		response += " Termites, aphids, white grabs and millipedes \n"
		response += " attack roots, stem base, leaves and pods.\n"
		response += "CONTOL: \n"
		response += "Early planting, observe farm hygiene, conserving natural enemies, \n"
		response += " timely harvesting, use well decomposed manure.\n"
		response += "Practice crop rotation, use certified seeds.\n"
		response += "HARVESTING:\n"
		response += "Harvest at 90days - 130days.\n"
		response += "Observe keeness at harvest to avoid breaking off.\n"
		response += "Dried well after shelling \nto avoid aflatoxin, pests and rot.\n"
		response += "MARKET YOUR PRODUCE.\n"
		response += "00. Send me in SMS.\n"
#Time to send an sms
	elif text == "1*1*1*00":
		try:
			#send an sms to user
			sms_response = sms.send("Sending you HOW-TO in SMS form ...", sms_phone_number)
			print(sms_response)
		except Exception as e:
			#show an error message
			print(f"Sorry, error occured: {e}")
	else:
		response = "END Invalid input. Try again."
	return response

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.environ.get("PORT"), debug="true")