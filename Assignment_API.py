######## ASSIGNMENT - API 
"""

Que1 : What is an API? Give an example, where an API is used in real life.

Ans : An, API or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate and interact with each other.
It utilizes the features and data of other services without having to understand the internal workings of those services.
Real life example of an API is Social Media Integration.
Suppose you want to share a blog post from your website directly to your social media account. Instead of manually copying and pasting the content, an API can be used to automate the process.
Your social media account provides an API that allows your website's backend to send a request with the content of the blog post, and in response, Social media account servers will post the content to your account.


Que 2 : Give advantages and disadvantages of using API.

Ans  : Advantages :
1. Allow developers to reuse the existing code and functionality without reinventing the wheel.
2. APIs provides a standardized way to access external services or data.
3. Enables access to external data sources.
4. Provides a platform for third-party developers to create applications, extensions that enhance the functionality of existing systems.

Disadvantages :
1. When using third-party APIs, you are entrusting your data to external services.
2. Some APIs comes with usage fees, like chatgpt openai. Integrating multiple paid APIs can increase operational costs.
3. Relying on external APIs can lead to dependency issue. If the API provider changes their service, your application could suffer from functionality loss or even break entirely.


Que 3 : What is a Web API? Differentiate between API and Web API.

Ans : WebAPI specifically refers to an API that is exposed over the internet using HTTP protocols. 
Web APIs are typically used for creating web services, allowing developers to integrate external services to their applications, mobile apps or websites.

Difference between Web API and API :
APIs can exist in various forms, not limited to a web based interactions.APIs can be designed for various contexts and interactions patterns.
But a WebAPI specifically focuses on remote interactions over the internet using HTTP
WebAPI is a type of API, not all APIs are necessarily WebAPIs.


Que 4: Explain REST and SOAP Architecture. Mention shortcomings of SOAP.

Ans : REST (Representational State Transfer):
It is an architectural style for designing networked applications, particularly web services, that emphasizes a stateless client-server interaction.
REST uses standard HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources, It is designed to be simple, scalable and well suited.

SOAP (Simple Object Access Protocol):
SOAP is a protocol for exchanging structured information in the implementation of web services. 
SOAP messages are typicaally formatted in XML and can be transmitted over various protocols including HTTP, SMTP and more.

Shortcomings of SOAP :
1. SOAP messages tend to more complex due to their XML- based structure, which can make parsing anf processing slower compared to other formats like JSON.
2. SOAP-based services are less cacheable due to dynamic XML content, which can impact performance.
3. It is less browser friendly in comparsion to REST, making it less suitable for web-applications.

Que 5 : Differentiate between REST and SOAP.

Ans 5 : 1. Rest do interactions between client and servers by using HTTP methods.
2. REST uses formats like JSON or XML for data exchange whereas, SOAP messages are usually in XML format with a rigid structure.
3. REST primarily uses HTTPS, FTP, and more. SOAP commonly uses HTTP ND SMTP.
4. In REST, resources are identified using URIs where in SOAP, messages don't inherently rely on URIs fir identification
5. REST is more browser friendly, but SOAP is less suitable 
6. REST generally performs better due to lightweight nature, suitable for mobile and web-applications.
whereas, SOAP can have more overhead to XML documenrs and additional protocol features.


"""