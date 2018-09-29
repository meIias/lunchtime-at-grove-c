/**
 * App.jsx
 *
 * - react app container, conditionally loads ui views
 */

import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

class App extends React.Component {

    render() {
        return (
            <div>
            </div>
        );
    }
}

/**
 * mounts App component on the DOM
 */
const initApp = () => {
    ReactDOM.render(
        <App />,
        document.getElementById("app")
    );
};

export default initApp;
