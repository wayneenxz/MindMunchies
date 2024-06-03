# Mind Munchies

## Proposed Level of Achievement
Apollo

## Motivation
In the hectic life of a university student, navigating diverse subjects with challenging concepts and terminology can be overwhelming. Our commitment is to offer learning opportunities that seamlessly integrate into students’ busy schedules. Recognizing the effectiveness of spaced repetition and active recalling for long-term retention, our platform provides effortless access to course content for continuous and efficient learning. Traditional study methods can be cumbersome, so we aim to inject vitality and engagement into academic learning through interactive and dynamic experiences. Our mission is to help students transcend time and space limitations, equipping them with technological tools to unlock their full academic potential.

## Aim
We aim to develop a robust and revolutionary platform that transforms mundane learning into a delightful experience. Initially targeting university students, our platform will integrate course materials to generate relevant and helpful flashcards using advanced algorithms. Teachers and students can also manually create flashcards to aid their learning journey. This interactive platform will enhance learning efficiency, making study sessions more engaging and productive. Our vision extends to expanding Mind Munchies to other professions and institutions, offering a flexible learning experience beneficial to all.

## User Stories
| User        | Intended Action           | Result |
| :-------------: |:-------------:| :-----:|
| Student      | Wants to optimize revision schedule | To maximize knowledge retention |
| Student      | Wants to be able to transform studying into a game      |  To have an interactive learning experience |
| Teacher | Wants to provide engaging and concise summaries     |  To help students absorb class content effectively |


## Features
1. **Educational Flashcard Generation**
   - Analyze course material to create bite-sized flashcards covering key concepts.
   - Algorithm can sieve through the input material and identify the main concepts to be highlighted.
   - Tutors can vet and adjust flashcards before student access.
   - Generate an optimal study schedule incorporating spaced repetition for long-term retention.

2. **Game-like Learning Environment**
   - Centralized platform for viewing flashcards by module.
   - Fun quizzes at the end of each topic to assess understanding.
   - Level and achievement system to incentivize academic tasks.
   - Adventure-type game system where user gets to choose their own character, with upgrades available with completion of quizzes.

3. **Unique Study Plan Tailored for Each Student**
   - Personalized study plans based on semester timetables and learning goals.
   - Machine learning analyzes performance to recommend study improvements.

4. **Community Forum**
   - Platform for module-specific content discussions.

5. **Learning Support**
   - Multi-language support, text-to-speech, and adjustable font sizes and types.

6. **API for Integration of External Applications**
   - Launch educational tools in the form of packages, fostering an academic collaboration ecosystem.
  
7. **Customizable Interface**
   - User would be able to customize the aesthetic and design of the interface to suit their academic needs.

## Features Priority List
| Must-have        | Good-to-have          | Could-have |
| :-------------: |:-------------:| :-----:|
| Educational Flashcard Generation      | Game-like Learning Environment | Customizable Interface |
| Unique Study Plan      | Community Forum    |   |
| Learning Support | API for Integration of External Applications     |   |

## Timeline

### Milestone 1: Technical Proof of Concept for Flashcard Generation
- Set up backend software infrastructure and database.
- Develop the user interface following UI and UX principles.
- Implement basic functions to generate flashcards from module input data.

### Milestone 2: Prototype (Core Features)
- Translate input data from three modules into functional flashcards and gamified quizzes.
- Simulate user testing for personalized study plans.
- Establish data infrastructure for storing and retrieving module data.

### Milestone 3: Extended System (Core + Extension Features)
- Functional community forums with user accounts and course modules.
- Multi-language support for the platform’s interface and content.
- Implement API endpoints and authentication mechanisms.
- Establish guidelines and data security for external applications.

## Tech Stack
- Java
- Python
- HTML
- CSS
- MySQL (Database)
- Blockchain

## Setup Guide
1. Install WampServer [here](https://sourceforge.net/projects/wampserver/)
2. In the installation page, WampServer requires certain elements to be installed before it can execute properly, namely. **Make sure you are "up to date" in the redistributable packages VC10, VC11, VC13, VC15 and VS16.** You may install these packages [here](https://wampserver.aviatechno.net/files/vcpackages/all_vc_redist_x86_x64.zip) using a Windows 64-bit machine.
3. In this repository, there is a folder named **'orbital'** with all the coding files required.
4. After installing, open your file explorer **C:\wamp64\www** and insert the **'orbital'** folder into the location.
5. Run WampServer.
6. Open your browser and type in the address **'localhost'**. It should bring you to the main page of WampServer. **'orbital'** should be visible under 'Your Projects'.
7. Click on **PhpMyAdmin**. Enter **'root'** as the username, with **'MySQL'** as the Server Choice.
8. Press Go
9. On the left, create a new schema called **'WebsiteLogin'**. Click into the schema.
10. Create a new table called **'LoginDetails'** with 5 columns.
11. In order, these are the columns of the table. **'id'** (INT), **'name'** (VARCHAR), **'username'** (VARCHAR), **'email'** (VARCHAR), **'password'** (VARCHAR).
12. Length/Values of the columns are free for you to set.
13. Now the Database should be set.
14. Enter **'localhost/orbital/login.php'** to access the site.
15. You may click **'Sign Up Now'**, which brings you to the Registration page.
16. After registering, you may now login! 



## Qualifications
- **Wayne:** Data visualization skills (BT1101), Python programming (CS1010A), product development (DTK1234), ethical considerations (IS1108).
- **Wen Xuan:** Data structures (CS2040S, CS2030S), JavaScript, CSS, HTML (CS50), ethical considerations (IS1108).

## Software Engineering
- **Iterative Development:** Regular iterations with thorough testing and feedback to adapt to changing requirements and prioritize features.
- **Continuous Integration and Continuous Deployment (CI/CD):** Automated testing and integration to ensure code quality and reduce errors.
- **Version Control:** Use of version control with branching strategies for managing feature development and code generation.
