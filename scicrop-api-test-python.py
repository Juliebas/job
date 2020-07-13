import json

sampleDict = {"full_name": "Julio Gabriel de Lima Silva","email": "juliebas@usp.br","mobile_phone": "+55 (11) 98033-5291","age": 19,"home_address": "35 Avenida Ede, Alto Porã","start_date": 1594470539,"opportunity_tag": "Estágio Python Developer","past_jobs_experience": "Trabalhei como Mecânico na Sambaíba Transportes Urbanos Ltda (Que diferença de empresgos né), fiquei lá por menos de um ano pois os horários da faculdade não batiam com o do trabalho","degrees": [{"institution_name": "Universidade de São Paulo","degree_name": "Instituto de Matemática e Estatística","begin_date": 1549008000,"end_date": 1701345600}, {"institution_name": "ETEC Horácio Augusto da Silveira","degree_name": "Tecnico de Mecânica Insdustrial","begin_date": 1454310000,"end_date": 1543591800}],"programming_skills": ["python", "javascript"],"database_skills": "mysql","hobbies": ["Basquete", "League of Legends"],"why": "Quero desenvolver minhas habilidades com novas linguagens","git_url_repositories": "Não tenho"}

jsonData = json.dumps(sampleDict)



import requests

response = requests.post('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume', json={"full_name": "Julio Gabriel de Lima Silva","email": "juliebas@usp.br","mobile_phone": "+55 (11) 98033-5291","age": 19,"home_address": "35 Avenida Ede, Alto Porã","start_date": 1594470539,"opportunity_tag": "Estágio Python Developer","past_jobs_experience": "Trabalhei como Mecânico na Sambaíba Transportes Urbanos Ltda (Que diferença de empresgos né), fiquei lá por menos de um ano pois os horários da faculdade não batiam com o do trabalho","degrees": [{"institution_name": "Universidade de São Paulo","degree_name": "Instituto de Matemática e Estatística","begin_date": 1549008000,"end_date": 1701345600}, {"institution_name": "ETEC Horácio Augusto da Silveira","degree_name": "Tecnico de Mecânica Insdustrial","begin_date": 1454310000,"end_date": 1543591800}],"programming_skills": ["python", "javascript"],"database_skills": "mysql","hobbies": ["Basquete", "League of Legends"],"why": "Quero desenvolver minhas habilidades com novas linguagens","git_url_repositories": "Não tenho"})


print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())
