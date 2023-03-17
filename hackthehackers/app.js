const express = require('express');
const bodyParser = require('body-parser')
const app = express();
const fs = require('fs');

// create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false })

// Middleware
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

// Set the view engine to use EJS
app.set('view engine', 'ejs');

// Serve static assets from the public directory
app.use(express.static('public'));

// Define routes for the application
app.get('/', (req, res) => {

    console.log(req.query);
    error_message = null
    try {
        const data = fs.readFileSync(req.query.error_file, 'utf8');
        error_message = data
      } catch (err) {
        error_message = null
      }
      console.log(error_message)
  res.render('index', { title: 'Home', error_message: error_message });
});

app.post('/join', (req, res) => {
    if (!req.body.link.includes('github')){
        console.log('nice try hacker');
    }

    return res.redirect('/?error_file=error1.txt')
  });

app.get('/about', (req, res) => {
  res.render('about', { title: 'About' });
});

app.get('/contact', (req, res) => {
  res.render('contact', { title: 'Contact' });
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
