from django.shortcuts import render
from django.contrib import messages
import openai

# Create your views here.

def home(request):
	lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup', 'markup-templating', 'matlab', 'mongodb', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex', 'ruby', 'rust', 'sass', 'scala', 'sql', 'swift', 'yaml']

	code=''
	lang=''


	if request.method == "POST":
		code = request.POST['code']
		lang = request.POST['lang']

		# Check to make sure they picked a lang
		if lang == "Select Programming Language":
			messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
			return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
		else:

			# OpenAI Key
			openai.api_key = ""

			# Create OpenAI Instance
			openai.Model.list()
			# Make an OpenAI Request
			try:
				response = openai.Completion.create(
					engine = 'text-davinci-003',
					prompt = f"Respond only with code. Fix this {lang} code: {code}",
					temperature = 0,
					max_tokens = 1000,
					top_p=1.0,
					frequency_penalty=0.0,
					presence_penalty=0.0,
					)
				# Parse the response
				response = (response["choices"][0]["text"]).strip()
				# Save To Database
				# record = Code(question=code, code_answer=response, language=lang, user=request.user)
				# record.save()

				return render(request, 'home.html', {'lang_list':lang_list, 'response':response, 'lang':lang})

							
			except Exception as e:
				# return render(request, 'home.html', {'lang_list':lang_list, 'response':e, 'lang':lang})
				return render(request, 'home.html', {'lang_list':lang_list, 'code':e, 'lang':lang})


	return render(request, 'home.html', {'lang_list':lang_list})


###################################################

def suggest(request):
	lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup', 'markup-templating', 'matlab', 'mongodb', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex', 'ruby', 'rust', 'sass', 'scala', 'sql', 'swift', 'yaml']

	code=''
	lang=''


	if request.method == "POST":
		code = request.POST['code']
		lang = request.POST['lang']

		# Check to make sure they picked a lang
		if lang == "Select Programming Language":
			messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
			return render(request, 'suggest.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
		else:

			# OpenAI Key
			openai.api_key = "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"

			# Create OpenAI Instance
			openai.Model.list()
			# Make an OpenAI Request
			try:
				response = openai.Completion.create(
					engine = 'text-davinci-003',
					prompt = f"Respond only with code {code}",
					temperature = 0,
					max_tokens = 1000,
					top_p=1.0,
					frequency_penalty=0.0,
					presence_penalty=0.0,
					)
				# Parse the response
				response = (response["choices"][0]["text"]).strip()
				# Save To Database
				# record = Code(question=code, code_answer=response, language=lang, user=request.user)
				# record.save()

				return render(request, 'suggest.html', {'lang_list':lang_list, 'response':response, 'lang':lang})

							
			except Exception as e:
				# return render(request, 'home.html', {'lang_list':lang_list, 'response':e, 'lang':lang})
				return render(request, 'suggest.html', {'lang_list':lang_list, 'code':e, 'lang':lang})


	return render(request, 'suggest.html', {'lang_list':lang_list})


