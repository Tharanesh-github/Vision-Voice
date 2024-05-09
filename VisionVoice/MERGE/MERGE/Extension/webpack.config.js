const path = require('path');

module.exports = {
    mode: 'production', // or 'production' depending on your environment
    entry: './src/background.js',
    output: {
        filename: 'background.bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            }
        ]
    }
};
