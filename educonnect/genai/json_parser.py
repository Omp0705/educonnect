import json

json_response = '''```json
[
    {
        "question": "What is the main purpose of Spring Boot?",
        "options": [
            "To simplify the development of Spring-based applications",
            "To provide a lightweight alternative to traditional Spring frameworks",
            "To enhance security in Spring applications",
            "To improve performance in Spring applications"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is a Spring Boot Starter?",
        "options": [
            "A pre-configured dependency that provides essential components for a specific application type",
            "A tool for creating custom Spring Boot applications",
            "A runtime environment for executing Spring Boot applications",
            "A configuration file for setting up Spring Boot applications"
        ],
        "correct_option": "A"
    },
    {
        "question": "Which annotation is used to mark the main class in a Spring Boot application?",
        "options": [
            "@SpringBootApplication",
            "@EnableAutoConfiguration",
            "@ComponentScan",
            "@Configuration"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the role of the `application.properties` file in Spring Boot?",  
        "options": [
            "To configure application settings",
            "To define dependencies for the application",
            "To specify the main class of the application",
            "To handle exceptions in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the primary purpose of the `@RestController` annotation?",       
        "options": [
            "To define a controller class for handling RESTful API requests",
            "To enable auto-wiring of beans",
            "To configure the application's data source",
            "To enable logging in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "Which annotation is used to map a method to a specific HTTP request?",   
        "options": [
            "@RequestMapping",
            "@GetMapping",
            "@PostMapping",
            "All of the above"
        ],
        "correct_option": "D"
    },
    {
        "question": "How can you create a custom Spring Boot Starter?",
        "options": [
            "By defining a new Maven module with specific dependencies and configurations",   
            "By using the `spring-boot-starter-parent` dependency",
            "By creating a new Spring Boot application with custom configurations",
            "By modifying the existing Spring Boot Starter dependencies"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the `@Autowired` annotation used for?",
        "options": [
            "To inject dependencies into a class",
            "To create a new bean instance",
            "To configure the application's data source",
            "To enable logging in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "How do you embed a Tomcat server within a Spring Boot application?",     
        "options": [
            "By adding the `spring-boot-starter-tomcat` dependency",
            "By configuring the Tomcat server in the `application.properties` file",
            "By creating a custom Tomcat server implementation",
            "By using the `Tomcat` class from the `org.apache.tomcat` package"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the role of the `@SpringBootApplication` annotation?",
        "options": [
            "To enable auto-configuration, component scanning, and the Spring Boot application context",
            "To define the main class of the application",
            "To configure the application's data source",
            "To handle exceptions in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the difference between `@GetMapping` and `@PostMapping`?",       
        "options": [
            "`@GetMapping` handles GET requests, while `@PostMapping` handles POST requests", 
            "`@GetMapping` is used for reading data, while `@PostMapping` is used for creating data",
            "Both annotations are used for the same purpose, but `@PostMapping` is more efficient",
            "None of the above"
        ],
        "correct_option": "A"
    },
    {
        "question": "How can you run a Spring Boot application?",
        "options": [
            "By using the `spring-boot:run` goal in Maven or Gradle",
            "By running the main class directly from your IDE",
            "By packaging the application as a JAR or WAR file and running it on a web server",
            "All of the above"
        ],
        "correct_option": "D"
    },
    {
        "question": "What is the purpose of the `@EnableAutoConfiguration` annotation?",      
        "options": [
            "To automatically configure beans based on dependencies found in the classpath",  
            "To enable component scanning",
            "To define the main class of the application",
            "To handle exceptions in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the `@Configuration` annotation used for?",
        "options": [
            "To mark a class as a source of bean definitions",
            "To enable auto-wiring of beans",
            "To configure the application's data source",
            "To enable logging in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "How can you create a REST endpoint that returns a JSON response?",       
        "options": [
            "By using the `@ResponseBody` annotation",
            "By using the `ObjectMapper` class to convert Java objects to JSON",
            "By using the `RestTemplate` class to make RESTful API calls",
            "All of the above"
        ],
        "correct_option": "A"
    },
    {
        "question": "What is the difference between `@RestController` and `@Controller`?",    
        "options": [
            "`@RestController` automatically converts response objects to JSON, while `@Controller` requires manual conversion",
            "`@Controller` is used for web applications, while `@RestController` is used for REST APIs",
            "Both annotations are used for the same purpose",
            "None of the above"
        ],
        "correct_option": "A"
    },
    {
        "question": "How can you connect to a database in a Spring Boot application?",        
        "options": [
            "By adding the appropriate database driver dependency and configuring the data source in `application.properties`",
            "By using the `JdbcTemplate` class to interact with the database",
            "By using the `EntityManager` class in JPA to interact with the database",        
            "All of the above"
        ],
        "correct_option": "D"
    },
    {
        "question": "What is the purpose of the `@ComponentScan` annotation?",
        "options": [
            "To scan for components, such as controllers, services, and repositories",        
            "To define the main class of the application",
            "To handle exceptions in the application"
        ],
        "correct_option": "A"
    },
    {
        "question": "How can you create a custom Spring Boot application?",
        "options": [
            "By using the Spring Initializr website or the `spring-boot-starter-parent` dependency",
            "By creating a new Maven or Gradle project and adding the necessary dependencies",            "By using the `spring-boot-cli` command-line interface",
            "All of the above"
        ],
        "correct_option": "D"
    }
]
```'''

def parse_questions(json_response):
    # Remove backticks and the word 'json'
    json_response = json_response.replace('```json', '').replace('```', '').strip()

    try:
        # Parse the JSON response
        questions = json.loads(json_response)

        # Initialize a list to store parsed question data
        parsed_questions = []

        # Iterate through each question in the JSON array
        for item in questions:
            question = item.get("question")
            options = item.get("options", [])
            correct_option = item.get("correct_option")

            # Append parsed data as a dictionary
            parsed_questions.append({
                "question": question,
                "options": options,
                "correct_option": correct_option
            })

        return parsed_questions

    except json.JSONDecodeError as e:
        print(f"Error parsing the response as JSON: {e}")
        return []

# parsed_questions = parse_questions(json_response)

# # Print the parsed questions
# for question in parsed_questions:
#     print(question)
