import PySimpleGUI as sg
import requests, bs4, datetime, docx

#make document name from current date
dt = datetime.datetime.now()
currentDate = (str(dt.month)+"."+str(dt.day)+"."+str(dt.year))
documentTitle = "Substack Scraper "+ currentDate + ".docx"

newDocument = docx.Document()

#adding a GUI
layout = [
    [sg.Text("Input link(s).")],      
    [sg.InputText(key="siteName", do_not_clear=False)],
    [sg.Button("Add to List")],
    [sg.Submit(), sg.Cancel()]]

window = sg.Window('Substack Article Scraper', layout)    
links = []
toggle = True #made toggle to create option to cancel program with notification popup

#create continuous window to accept links and add them to scraper list until the user clicks the Submit button
while True:
    event, values = window.read()
    if event == "Submit" and len(links) == 0:
        sg.popup("You need to add links to scrape.")
    elif event == "Submit":
        break
    elif event == sg.WIN_CLOSED or event == 'Cancel':
        toggle = False
        break
    elif event == "Add to List":
        links.append(values["siteName"]) #add link from text box into list


window.close()       

#request each website from the new links list, make objects, get text
for articlePages in links:
    pageRequest = requests.get(articlePages)
    pageRequest.raise_for_status()
    soup = bs4.BeautifulSoup(pageRequest.text, features='lxml')

    #grabbing element objects
    dateElements = soup.time
    paragraphElements = soup.find_all("p")
    

    #turning elements into usable text
    documentHeader = soup.find("h1", class_="post-title short unpublished")
    documentDates = dateElements.get_text(" ", strip=True)
    
    
    #document writing
    newDocument.add_heading(documentHeader, 2)
    newDocument.add_paragraph(documentDates)
    for paragraphs in paragraphElements:
        newDocument.add_paragraph(paragraphs.get_text(strip=True))

if toggle == True:
    newDocument.save(documentTitle)
    sg.popup("Success! The document will be found in the same folder where the program is.")
else:
    sg.popup("Operation cancelled.")
