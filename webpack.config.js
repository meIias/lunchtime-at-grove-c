const path = require('path');

module.exports = {
    entry: './static/js/index.js',
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: 'dist.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: "babel-loader"
            },
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: "babel-loader"
            }
        ]
    }
};
