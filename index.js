const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./db'); 

// Initialize app
dotenv.config();
const app = express();

// Connect to MongoDB
connectDB(process.env.MONGO_URI);

// Basic route
app.get('/', (req, res) => {
    res.send('API is running...');
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
