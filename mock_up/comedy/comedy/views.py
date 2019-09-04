from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from time import sleep
# from chatterbot import ChatBot

# chatbot = ChatBot(
#     'Ron Obvious',
#     trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
# )

# Train based on the english corpus

#Already trained and it's supposed to be persistent
#chatbot.train("chatterbot.corpus.english")

day_maker_responses = [
	'Where will this concert be?',
	'Okay, how will you be getting around when you’re at the concert?',
	'Would you like to do anything before or after?',
	'What type of food would you like?',
	'How much would you like spend $, $$, or $$$?',
	'Based on your suggestions I recommend:\n \
		- Diaspora at 2118 N High St, Columbus, OH 43201 based on your interest in sushi and $\n \
		- Cazuela’s at 2321 N High St, Columbus, OH 43202 based on your interest in Mexican food and $\n \
		- Chipotle at 2130 N High St, Columbus, OH 43201 based on your interest in Mexican food and $',
	'Awesome! Right now you’re going to Diaspora then to your concert from 8-11:30. Do you want to plan anything else for that day?',
	'What kind of atmosphere would you like this bar to have?',
	'How much would you like spend $, $$, or $$$?',
	'Based on your suggestions I recommend:\n \
		- The Thirsty Scholar at 2201 Neil Ave, Columbus, OH 43201 based on chill atmosphere and $\n \
		- The Library Bar at 2169 N High St, Columbus, OH 43201 based on chill atmosphere and $\n \
		- The Old North Arcade at 2591 N High St, Columbus, OH 43202 based on chill atmosphere and $',
	'The Library is a vintage, old-school sports bar providing daily drink specials, plus pinball machines & pool tables.',
	'Based on your suggestions I recommend:\n \
		- The Thirsty Scholar at 2201 Neil Ave, Columbus, OH 43201 based on chill atmosphere and $\n \
		- The Little Bar at  2195 N High St, Columbus, OH 43201 based on chill atmosphere and $\n \
		- The Old North Arcade at 2591 N High St, Columbus, OH 43202 based on chill atmosphere and $',
	'Cool! Right now you’re going to Diaspora then to your concert from 8-11:30 followed by The Old North Arcade. Do you want to plan anything else for that day?',
	'Your evening plans for Friday are:\n \
		- Diaspora at 2118 N High St, Columbus, OH 43201\n \
		- Concert at 555 Borror Dr, Columbus, OH 43210\n \
		- The Old North Arcade at 2591 N High St, Columbus, OH 43202'
	]

@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body)
		# message = data['message']
		# chat_response = chatbot.get_response(message).text
		sleep(0.75)
		chat_response = day_maker_responses.pop(0)
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request, template_name="home.html"):
	context = {'title': 'Chatbot Version 1.0'}
	return render_to_response(template_name, context)
