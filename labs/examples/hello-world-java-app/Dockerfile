#FROM openjdk:8-jre
#FROM openjdk:11-jre
#FROM openjdk:17
FROM openjdk:17-slim

LABEL version="1.0"
LABEL description="Hello World App Image"
COPY ./target/hello-world-app-jar-with-dependencies.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]