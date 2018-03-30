# SentimentMessenger
In today’s world of cut throat competition, for any company to out maneuver competition it should know how its product is perceived by the customers. And that has bestowed huge responsibility on the shoulders of Marketing Team. To ease their burden, I have developed a Sentiment Messenger, which can help them to converse with customers intelligently with help of Microsoft Sentiment API.
I have used Microsoft Sentiment API to calculate sentiment of the customer’s feedback to respond them with an apt reply. The threshold for positive response is kept at greater than 0.5. For having a messaging capability for my application, I have taken help from Twilio API, enabling this application to have conversation with anyone in US.
Python is used to support backend for this application. It enabled me for better API integration and a smooth interface. MongoDB was used to support data handling capability for the application. MongoDB has helped in hosting data about the Marketing Team’s user, Customer with their product, Messaging Template with their respective Marketing user. 
The application is hosted on AWS server to have universal access and have scalability. The application will enable Marketing team to function and converse with customer with ease.

# Steps:
1.	Visit the site at http://18.216.222.217 for accessing the application interface.
2.	Register for a new user or login with username: smitp and password: !@#123.
3.	After login you will the reach the main page “Dashboard”, here you can have access of functionality to have conversation with the customers.
4.	In left pane of dashboard, you can enter cell number of a customer in format “+19999999999” and customer’s name to send them personalized message.
5.	In the right pane you will see default message templates for each user.
6.	You can edit them, but keep the tags same to create the personalized message.
a.	Tags: <firstName> and <productType>
7.	Press “send” button to send message to the customer with personalized message.
8.	Based on the customers reply, whether positive or negative the application will respond them with appropriate message based on the template, to get the cause of their feeling about the product.
9.	You can logout from session after your job is done.

# Future:
This is the initial product. It can have an added functionality of being a chatbot, that can have a full end to end conversation with the multiple customers and can make the analysis about all products with their drawbacks and strong features. Application can in future give the final analysis report about the product to the marketing team to help them make better business decision.
