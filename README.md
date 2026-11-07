<<<<<<< HEAD
# Tour Package Management System

Student: Raina Joshy  
Register Number: CCE25CS208

A Django CRUD application with signup, login, logout, and protected package-management pages.

## 1. Setup

Install Python 3.10+ and open a terminal in this folder.

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

Install Django and prepare the database:

```bash
pip install -r requirements.txt
python manage.py makemigrations packages
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## 2. First use

1. Select **Sign up** and create a username/password.
2. Log in.
3. Add, view, edit, or delete tour packages.
4. Use **Logout** to end the session.

## 3. Project structure

```text
tourproject/
    settings.py
    urls.py
    wsgi.py
    asgi.py
packages/
    migrations/
    templates/packages/
    static/packages/css/style.css
    static/packages/js/validation.js
    models.py
    forms.py
    views.py
    urls.py
```

## 4. Notes

- Package fields follow the question paper: `package_name`, `destination`, `duration`, and `price`, all as `CharField`.
- Django's built-in `UserCreationForm`, authentication views/functions, and `@login_required` are used.
- The add/edit form validates that no field is empty in both the browser and server.
- For submission, rename the outer project folder to include your name and register number if your instructor requires it.
=======
# 💫 About Me:
🔭 I’m currently working on Learning the basics of programming and computer science concepts.<br>👯 I’m looking to collaborate on Beginner-friendly coding projects or study groups.<br>🤝 I’m looking for help with Getting guidance on how to start building simple projects.<br>🌱 I’m currently learning fundamentals about programming.<br>💬 Ask me about My journey as a beginner in coding.<br>⚡ Fun fact I’m excited to write my first “Hello, World!” program soon!


# 💻 Tech Stack:
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![AssemblyScript](https://img.shields.io/badge/assembly%20script-%23000000.svg?style=for-the-badge&logo=assemblyscript&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white) ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white) ![OpenStack](https://img.shields.io/badge/Openstack-%23f01742.svg?style=for-the-badge&logo=openstack&logoColor=white) ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![CockroachLabs](https://img.shields.io/badge/Cockroach%20Labs-6933FF?style=for-the-badge&logo=Cockroach%20Labs&logoColor=white) ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white) ![PlanetScale](https://img.shields.io/badge/planetscale-%23000000.svg?style=for-the-badge&logo=planetscale&logoColor=white) ![PocketBase](https://img.shields.io/badge/pocketbase-%23b8dbe4.svg?style=for-the-badge&logo=Pocketbase&logoColor=black) ![Prisma](https://img.shields.io/badge/Prisma-3982CE?style=for-the-badge&logo=Prisma&logoColor=white) ![Sequelize](https://img.shields.io/badge/Sequelize-52B0E7?style=for-the-badge&logo=Sequelize&logoColor=white) ![AmazonDynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white) ![Appwrite](https://img.shields.io/badge/Appwrite-%23FD366E.svg?style=for-the-badge&logo=appwrite&logoColor=white) ![Adobe Illustrator](https://img.shields.io/badge/adobe%20illustrator-%23FF9A00.svg?style=for-the-badge&logo=adobe%20illustrator&logoColor=white) ![Adobe](https://img.shields.io/badge/adobe-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white) ![Adobe Acrobat Reader](https://img.shields.io/badge/Adobe%20Acrobat%20Reader-EC1C24.svg?style=for-the-badge&logo=Adobe%20Acrobat%20Reader&logoColor=white) ![Adobe Audition](https://img.shields.io/badge/Adobe%20Audition-9999FF.svg?style=for-the-badge&logo=Adobe%20Audition&logoColor=white) ![Adobe Lightroom](https://img.shields.io/badge/Adobe%20Lightroom-31A8FF.svg?style=for-the-badge&logo=Adobe%20Lightroom&logoColor=white) ![Rhinoceros](https://img.shields.io/badge/Rhinoceros-801010?style=for-the-badge&logo=rhinoceros&logoColor=white) ![Adobe Lightroom Classic](https://img.shields.io/badge/Adobe%20Lightroom%20Classic-31A8FF.svg?style=for-the-badge&logo=Adobe%20Lightroom%20Classic&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Scipy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Epic Games](https://img.shields.io/badge/epicgames-%23313131.svg?style=for-the-badge&logo=epicgames&logoColor=white) ![Godot Engine](https://img.shields.io/badge/GODOT-%23FFFFFF.svg?style=for-the-badge&logo=godot-engine) ![Humble Bundle](https://img.shields.io/badge/HumbleBundle-%23494F5C.svg?style=for-the-badge&logo=HumbleBundle&logoColor=white) ![Plex](https://img.shields.io/badge/plex-%23E5A00D.svg?style=for-the-badge&logo=plex&logoColor=white) ![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=for-the-badge&logo=firefox&logoColor=#FF7139) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white) ![Jellyfin](https://img.shields.io/badge/jellyfin-%23000B25.svg?style=for-the-badge&logo=Jellyfin&logoColor=00A4DC) ![Babel](https://img.shields.io/badge/Babel-F9DC3e?style=for-the-badge&logo=babel&logoColor=black) ![Alfred](https://img.shields.io/badge/alfred-%235C1F87.svg?style=for-the-badge&logo=alfred) ![FFmpeg](https://shields.io/badge/FFmpeg-%23171717.svg?logo=ffmpeg&style=for-the-badge&labelColor=171717&logoColor=5cb85c) ![Analogue](https://img.shields.io/badge/Analogue-1A1A1A?style=for-the-badge&logo=Analogue&logoColor=white) ![Uber](https://img.shields.io/badge/Uber-%23000000.svg?style=for-the-badge&logo=Uber&logoColor=white) ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Packer](https://img.shields.io/badge/packer-%23E7EEF0.svg?style=for-the-badge&logo=packer&logoColor=%2302A8EF) ![Mosquitto](https://img.shields.io/badge/mosquitto-%233C5280.svg?style=for-the-badge&logo=eclipsemosquitto&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Unity](https://img.shields.io/badge/unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white) ![PlayStation Network](https://img.shields.io/badge/PSN-%230070D1.svg?style=for-the-badge&logo=Playstation&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white) ![GitLab CI](https://img.shields.io/badge/gitlab%20CI-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white) ![CircleCI](https://img.shields.io/badge/circleci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white) ![TeamCity](https://img.shields.io/badge/teamcity-000000.svg?style=for-the-badge&logo=teamcity&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Apache Hadoop](https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black) ![Context-API](https://img.shields.io/badge/Context--Api-000000?style=for-the-badge&logo=react) ![EJS](https://img.shields.io/badge/ejs-%23B4CA65.svg?style=for-the-badge&logo=ejs&logoColor=black) ![Fastify](https://img.shields.io/badge/fastify-%23000000.svg?style=for-the-badge&logo=fastify&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Pug](https://img.shields.io/badge/Pug-FFF?style=for-the-badge&logo=pug&logoColor=A86454) ![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white) ![JavaFX](https://img.shields.io/badge/javafx-%23FF0000.svg?style=for-the-badge&logo=javafx&logoColor=white) ![Apache Tomcat](https://img.shields.io/badge/apache%20tomcat-%23F8DC75.svg?style=for-the-badge&logo=apache-tomcat&logoColor=black) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white) ![Apache Ant](https://img.shields.io/badge/Apache%20Ant-A81C7D?style=for-the-badge&logo=Apache%20Ant&logoColor=white) ![Nx](https://img.shields.io/badge/nx-143055?style=for-the-badge&logo=nx&logoColor=white) ![WordPress](https://img.shields.io/badge/WordPress-%23117AC9.svg?style=for-the-badge&logo=WordPress&logoColor=white) ![Web3.js](https://img.shields.io/badge/web3.js-F16822?style=for-the-badge&logo=web3.js&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=rainajoshy&theme=dark&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://nirzak-streak-stats.vercel.app/?user=rainajoshy&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=rainajoshy&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

---
[![](https://visitcount.itsvg.in/api?id=rainajoshy&icon=0&color=0)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->
>>>>>>> 818a84ed875c79b1a976d0139f533f9281360afd
