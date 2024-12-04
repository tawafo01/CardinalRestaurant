# CardinalRestaurant
CSE 350 Project: Cardinal Restaurant
![Cardinal Bird](images/Cardinal.jpg)

Section: CSE-350-50-4248

Team Members: Tanner Waford, Saketh Sangaraju, Sraddha Patri, Huy Truong, Adam McCabe

Group Number: 10

Overview: 
A two-way POS (Point of Service) application to be used by the students, dining services staff, and university administation of the University of Louisville, to improve the dining experience.
Students will be able to purchase menu items and get recommendations from a generative AI chatbot (keeping in mind dietary restrictions, pricing, etc.).
Dining services are able to leverage the software to keep track of transactional information in a database for more efficient order processing.

Description:
The objective of this project is to create a two-way interface that serves both the University of Louisville (UofL) students and Cardinal Dining Services. The system is designed to streamline food ordering and provide personalized recommendations while maintaining an intuitive user experience. For students, the interface’s goal is to simplify the process of browsing and ordering food by integrating a chatbot powered by the GROQ API, which offers recommendations based on specific criteria, like available Flex Points, dietary restrictions, and ingredient preferences. For Cardinal Dining Services, the system uses efficient transaction management, allowing restaurant staff to process orders seamlessly and maintain organized financial stats. 
A vital part of the system is the integration of an AI chatbot that interacts with students to provide recommendations tailored to their preferences. By using the GROQ API, the chatbot can dynamically retrieve information about menu items, including their ingredients and prices. This personalized interaction not only enhances user satisfaction but also encourages informed food choices based on individual needs and budgets.
The project also includes the development of a user-friendly graphical user interface (GUI) built with Python's Tkinter library. This interface will cater to both customers and vendors. For students, the GUI will allow them to navigate the menu easily, select food items, and continue with secure payments. For dining services staff, the interface will support order management and menu updates, ensuring efficient back-end operations.
To ensure the system is reliable, we had a testing scheme planned. This scheme uses several critical components. First, the order payment calculator will be tested by taking a sample of items and verifying the calculated prices for accuracy. Second, the GROQ API integration will be evaluated by initiating chats with the AI to confirm the correct call-and-response functionality, particularly in handling food-related queries and database values. Third, the GUI menu selection will be tested to verify that it displays all correct information—such as ingredients and prices—for each selected item, and that the navigation is intuitive.
Error handling is another key focus of the testing strategy. Simulated scenarios, such as selecting invalid menu items, experiencing network failures during API calls, or encountering payment processing issues, will be employed to ensure that appropriate error messages are displayed to the user. These tests are designed to guarantee that the system can manage unexpected situations while maintaining a positive user experience.
To summarize, the success of this project is dependent on the integration of its different components into an integrated system. By meeting the demands of both students and Cardinal eating Services, the two-way interface aims to set a new standard for campus dining technology. A strong chatbot powered by the GROQ API, a functional and visually appealing GUI, and rigorous testing processes ensure that the final product is both dependable and user-friendly.
