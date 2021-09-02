import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def analyse(name):
# Open pdf file
    pdfFileObj = open(name,'rb')

    # Read file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Get total number of pages
    num_pages = pdfReader.numPages

    # Initialize a count for the number of pages
    count = 0

    # Initialize a text empty etring variable
    text = ""

    # Extract text from every page on the file
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()


    # Convert all strings to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+','',text)

    # Remove punctuation
    text = text.translate(str.maketrans('','',string.punctuation))


    terms = {'Web Designing & Development':['html','css','javascript','django','flask','bootstrap',
                                'node.js', 'react.js','angular.js','express.js','php'],      
            'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                    'machinery','maintenance','manufacture','line balancing','oee','operations',
                                    'operations research','optimization','overall equipment effectiveness',
                                    'pfmea','process','process mapping','production','resources','safety',
                                    'stoppage','value stream mapping','utilization'],
            'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                            'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                            'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                            'third party logistics','transport','transportation','traffic','supply chain',
                            'vendor','warehouse','wip','work in progress'],
            'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                                'finance','kanban','leader','leadership','management','milestones','planning',
                                'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders'],
            'Data Science & ML':['analytics','api','aws','big data','busines intelligence','clustering',
                            'data','database','data mining','data science','deep learning','hadoop',
                            'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                            'predictive','programming','python','r','sql','tableau','text mining',
                            'visualuzation','pandas','numpy','scikit-learn','sklearn','linear regression'],
            'Database Management Systems':['mysql','sqlite','nosql','mongodb','sql','oracle']}



    web = 0
    operations = 0
    supplychain = 0
    project = 0
    data = 0
    database_management_systems = 0

    # Create an empty list where the scores will be stored
    scores = []

    # Obtain the scores for each area
    for area in terms.keys():
            
        if area == 'Web Designing & Development':
            for word in terms[area]:
                if word in text:
                    web +=1
            scores.append(web)
            
        elif area == 'Operations management':
            for word in terms[area]:
                if word in text:
                    operations +=1
            scores.append(operations)
            
        elif area == 'Supply chain':
            for word in terms[area]:
                if word in text:
                    supplychain +=1
            scores.append(supplychain)
            
        elif area == 'Project management':
            for word in terms[area]:
                if word in text:
                    project +=1
            scores.append(project)
            
        elif area == 'Data Science & ML':
            for word in terms[area]:
                if word in text:
                    data +=1
            scores.append(data)
            
        elif area == "Database Management Systems":
            for word in terms[area]:
                if word in text:
                    database_management_systems +=1
            scores.append(database_management_systems)

    summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)

    return summary

    '''pie = plt.figure(figsize=(10,10))
    plt.pie(summary['score'], labels=summary.index, explode = (0.1,0,0,0,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
    plt.title('Industrial Engineering Candidate - Resume Decomposition by Areas')
    plt.axis('equal')
    return plt.show()'''

    # Save pie chart as a .png file
    #pie.savefig('resume_screening_results.png')'''