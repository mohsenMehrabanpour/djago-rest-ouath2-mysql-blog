<b><i>this project developed by :</i></b>
<ul>
<li><i>django rest framework</i></li>
<li><i>mysql database</i></li>
<li><i>django ORM</i></li>
<li><i>django Mails (SMTP protocol)</i></li>
<li><i>redis database</i></li>
<li><i>celery Async tasks</i></li>
</ul>
<hr>

<h3>how to register with confrim email in this project</h3>
<b>first step: </b>
<br>
send a <b>POST</b> request to <code>/profile/register/</code> with a <mark>JSON</mark> body that contains:<br><br>
<code>{
    "username":"something",
    "password":"something",
    "first_name":"something",
    "last_name":"something",
    "email":"somethig@gmail.com",
    "phone_number" : "09*********"
}
</code>
<br><br>
<b>second step: </b>

it will response you with a JSON that contains:
<br><br>
<code> {'verify_request_key': "the key"} </code>

<br><br>
<b>third step: </b>
<br>
then you will recive an email that contain your verfication code , for confrim your email you have to send a <b>POST</b> request to <code> /profile/register/verify </code>
with a JSON that contains :
<br><br>

<code>
{
    "verify_request_key": "the key you recived in second step",
    "client_verification_code": "the code in your email"
}
</code>

<h1> Dont forget </h1>
for using this project surly you have to set <cpde>EMAIL_ADDRESS</code> and <cpde>EMAIL_password</code>
you can set them and other variable in <code>local_config.py</code> file
<br>
<ul>
<li>you have to run <code> celery workers </code></li>
<li>you have to run <code> manage.py runserver </code></li>
<li>you have to install <code> requirement.txt </code></li>
</ul>




