[![Flask Landing Project](https://static.codingforentrepreneurs.com/media/projects/flask-landing/images/share/Flask_Landing.jpg)](https://www.codingforentrepreneurs.com/projects/flask-landing/)

# Flask Landing
Learn to build a landing page with the very popular Python Flask Microframework.


#### Lesson Code
This is what the code looks like at the end of the lesson. It's made for your reference so you can see a history of changes.

1. Welcome & Requirements _no code_

2. Walkthrough _no code_

3. Create a Virtual Environment _no code_

4. Sublime Text & Reactivate Virtual Environment

[5 - Hello World with Flask](../../tree/e0b1bae98738c6ab93ccf913eedacbf62dbc0b23/)

[6 - WSGI for Local Dev](../../tree/00fb9c3c51033e54d6e732dd9db65ef181a37acf/)

[7 - URL Routing](../../tree/673af3942b11d1d44605806c3fac26a00d511b4f/)

[8 - Flask App as Package](../../tree/18fbffadea20e83513da3847f6b23c48c8f44a1f/)

[9 - Modules Driving One Purpose](../../tree/bf9019d97cb55e73b59d34a9be251e7fbe4ca0aa/)

[10 - Render HTML Template](../../tree/c6737068a09f5358ef72d086d0b6f761c70b3aeb/)

[11 - Render Template Variables](../../tree/fb1b4cdaf6c7f08b4b7f75a15eda2c43448e5d65/)

[12 - Keep Logic in Views not Templates](../../tree/73db8b26456ecc8e871032044201a60956107772/)

[13 - Jinja Templates & Base HTML](../../tree/eafb22b8625bc3ca45d6fdf7d2f7f1243d66671a/)

[14 - Render JSON](../../tree/408e5d924f56dcfb905f7ccfe61ff71bc63e8f96/)

[15 - Landing Page Form](../../tree/d88a0cce5df34b566f1880db658f13386c326856/)

[16 - POST Method and Request Data](../../tree/1989f28a78360583ef3b640c0dd867cff29fbff6/)

[17 - Validation & CSRF](../../tree/3ecb4a0d2758c540f0b6b098067059adf0d0bb6e/)

[18 - Python eval](../../tree/d7b13b28124af76148fa9342ef6114b68abec01e/)

[19 - Adding CSRF Protection to Flask](../../tree/ff80d1549787d2a1f13661941e71ee15b46eb3c9/)

[20 - A Form with Flask WTF](../../tree/7ee56db3e7633048cf5d0aa2520435e3a2d03ba1/)

[21 - Basic Form Validation with wtforms](../../tree/f5bf3c1fbbf6a05897c309efe3e909d83307f1de/)

[22 - Email & Custom Validation with wtforms](../../tree/028b783848ed6e8f108557e2162874dedc90d33a/)

[23 - Render the Flask WTF Form in Template](../../tree/8de49fcad740e8c064e2d03b16b1c09ea5e3c672/)

[24 - Input Class and Placeholder in Flask WTF Forms](../../tree/7b726a6020a6afd9665a3f664a1e9feca35de57c/)

[25 - Setup a Database.](../../tree/2e3407349bf1c2856f5185fff4f4066bf12e3e3f/)

[26 - Your First SQLAlchemy Model](../../tree/22aef7ac1b85c8b91ae6302231a428c92bf43cec/)

[27 - Save to Database](../../tree/80f45ba6f6b91e63de0e651791dd56aebc65ac0d/)

[28 - Track Modification Error](../../tree/f85ab67a848a1e933e90dbd6f4f1adad5dad734b/)

29 - Database Actions in Flask Shell _no code_

[30 - Convenience Methods for CRUD](../../tree/40bef5eed2c5f26597ab8d8cfc27ae222bf06ab1/)

[31 - Saving Data to a Model via a Form](../../tree/67ff9521c1fa1b59f8ee24f187edf0eb93fca2f1/)

[32 - Validation Form against Database with Model Lookup](../../tree/4b18028a0400202eda2348e1813e271ced21b0cd/)

[33 - Database Object to Detail View](../../tree/66f835df39c0b1ce1c686ad4870262c7dc24f457/)

[34 - First or 404](../../tree/6bd31ec341f0a393bd99b38b301ed50d459a584b/)

[35 - Update View and Prefill Form Data](../../tree/be5f10208f1c570c76dedda7029c3069fc7b5e52/)

[36 - Save Updates in Update View](../../tree/a4c49e8609a32912a1023228030fd7e6613c1ca2/)

[37 - Exclude Items from SQLAlchemy Query](../../tree/3089738bc2bb51654544c18c4c564fba1d774999/)

[38 - Delete & Confirm](../../tree/cfca3cae6dee29c28ea215a96a48cc0ca805befb/)

[39 - List View and Redirects](../../tree/4facdfad3716f9cdb587fe3b0c98ea765c162b7d/)

[40 - Navbar with Include](../../tree/a599b78bbec3f92e342c92fe77fc9c63d4c603ef/)

[41 - Dynamic URL Paths with url_for](../../tree/670fd920a08d91c620d83715a33e45549482cb91/)

[42 - url_for with Arguments](../../tree/dde3a97252e2cf9a9da421d3a445271f27d7de15/)

[43 - Signals](../../tree/83c9e403f648f6d9802efbef098c93aa09e15ffa/)

[44 - Change Models with Flask Migrate](../../tree/1855bfed2d305b5a04d22cf3e6fb690da75a14f4/)

[45 - Fresh Migrate and DB](../../tree/e52416b57d029d08cc093358a9278e39e6f99860/)

[46 - Migrate Again](../../tree/da69781001544f584e5f154776280a20d35596f6/)

[47 - Password Protect a View](../../tree/fa5dd457296e6867c11891bd9d27f8bcb214ff02)

[48 - Prep Landing Page for Production](../../tree/4bbadfb22c79d715fd392eec1243068b709a029b)

[49 - Gunicorn Server](../../tree/02172e4ca126acf87e3454d5260ce9df8c125a3f)

[50 - Heroku and Live App](../../tree/0abc3be684d974e7a94e07944ae57cbee0d64f20)

[51 - Making Changes for Production](../../tree/4e86345148d84b0ea4513a67be2575bc7d85325f)

52 - Custom Domain
```console
heroku domains:add
```

53 - Adding HTTPs using [ACM](https://devcenter.heroku.com/articles/automated-certificate-management)
```console
heroku ps:resize web=hobby

heroku certs:auto:enable
```

[54 - Suggested Next Steps](../../tree/45d1da542aeea47e8554df306747d844a2a42279)
