

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 5000;


mongoose.connect('mongodb+srv://Ayush:Ayush123@cluster0.mm5itwq.mongodb.net/AOH')
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));
app.use(bodyParser.json());

app.use('/api/auth', require('./routes/auth'));

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
