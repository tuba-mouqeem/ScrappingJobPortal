from bs4 import BeautifulSoup

with open('home.html') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml') 
    # print(soup.prettify()) # prettify() method is used to make the HTML content look more readable. 
    # courses_html_tags = soup.find_all('h5')
    # # tags = soup.find('h5')
    # print(courses_html_tags)
    
    # for course in courses_html_tags:
    #     print(course.text)
    
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}')
        