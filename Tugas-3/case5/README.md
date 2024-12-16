# Weather Forecast Web Application with DevOps Pipeline

## Overview
Welcome to the Weather Forecast Web Application! This project demonstrates my expertise as a DevOps engineer by combining various technologies to deliver a seamless and automated software development and deployment process.

The Weather Forecast Web Application allows users to retrieve accurate weather forecasts for the next 7 days based on their location input. It utilizes the OpenWeatherMap API to fetch weather data and presents it in an intuitive and user-friendly interface.
<br/>
<br/>
![App Screenshot](https://github.com/shmuelSigler/Jenkins_Docker_Slack/blob/main/weather%20app%20screenshot.png?raw=true)

## Key Features
- **Weather Forecast**: Get a 7-day weather forecast for a specified city or country.
- **Automated Pipeline**: Jenkins orchestrates a fully automated pipeline, from code integration to deployment.
- **Docker Integration**: The application is containerized using Docker, ensuring consistent deployment across environments.
- **Slack Integration**: Real-time communication is facilitated through Slack, providing visibility into pipeline status.
- **Continuous Testing**: Jenkins performs unit tests to ensure the reliability of each deployment.
- **Seamless Deployment**: Automated deployment to AWS EC2 instances keeps the application up-to-date.

## NGINX and Gunicorn Integration
To enhance the performance and reliability of the Weather Forecast Web Application, NGINX and Gunicorn have been integrated into the project. NGINX acts as a reverse proxy server, forwarding requests to Gunicorn, which serves the application. This setup provides benefits such as load balancing, improved security, and better handling of client connections.

### NGINX Configuration
The NGINX configuration plays a significant role in directing incoming traffic to the appropriate backend servers. In my project, NGINX is set up as a reverse proxy, which means it receives client requests and forwards them to the Gunicorn instances running the Python application. Let's take a closer look at the key components of my NGINX configuration:

- **limit_req_zone and limit_conn_zone**: These directives define rate limiting and connection limiting zones to manage the rate at which clients can access the application. <ins>This helps prevent abuse and ensures fair usage.</ins>
- **upstream**: The upstream block defines a group of backend servers (Gunicorn instances) that NGINX can direct traffic to. In my case, i've specified two instances (weather_app-app-1 and weather_app-app-2) to <ins>distribute the load and ensure high availability.</ins>
- **server**: This block specifies the configuration for the virtual server that listens on port 80. It includes directives <ins> to manage rate limiting and connection limiting</ins>, as well as the proxy_pass directive, which forwards incoming requests to the backend Gunicorn instances.


## Project Architecture and Components

![Architecture](https://github.com/shmuelSigler/Jenkins_Docker_Slack/blob/main/architecture.png?raw=true)

- Executed a comprehensive project involving GitLab and Jenkins servers, showcasing my expertise in streamlining development workflows. 
- Developed and implemented a Jenkins pipeline for the Weather app, effectively integrating remote GitLab repositories. 
- Demonstrated proficiency in automating the build process by creating Docker images and conducting rigorous unit tests. 
- Successfully deployed the tested images to Docker Hub, emphasizing my ability to ensure reliable software delivery. 
- Leveraged Slack integration to facilitate real-time communication and enhance collaboration within the development team. 
- Skillfully configured Jenkins to provide notifications on pipeline success, showcasing my attention to detail and dedication to delivering quality results. Implemented error handling mechanisms to promptly address any pipeline failures, exhibiting my problem-solving skills and ability to troubleshoot issues efficiently.



#### Contact
For any inquiries or questions, please reach out to yakovsig@gmail.com.

## Run Locally

Clone the project

```bash
  git clone https://github.com/shmuelSigler/Jenkins_Docker_Slack.git
```

Go to the project directory

```bash
  cd Jenkins_Docker_Slack
```

Run docker compose to start Docker containers defined in a Compose file

```bash
  docker compose up -d
```

  ## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
`API_KEY`

<a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/lnviuuso7dnvqyp0pv3l" alt="trackgit-views" />
</a>
