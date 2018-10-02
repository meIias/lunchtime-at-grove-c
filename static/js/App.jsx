/**
 * App.jsx
 *
 * - react app container, conditionally loads ui views
 */

import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import axios from 'axios';

import UserForm from './UserForm.jsx';
import LunchCoffeeForm from './LunchCoffeeForm.jsx';
import AppContainerCard from "./AppContainerCard.jsx";

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: "",
            userAdded: false,
            userActionResult: ""
        };
        this.handleUserSet = this.handleUserSet.bind(this);
        this.isUsernameValid = this.isUsernameValid.bind(this);
        this.handleUsernameChanged = this.handleUsernameChanged.bind(this);
        this.handleCoffeeLunchOptionSelected = this.handleCoffeeLunchOptionSelected.bind(this);
    }

    /**
     * callback for when user input is complete
     */
    handleUserSet() {
        this.setState({
            userAdded: true
        });
    }

    /**
     * callback to set username
     */
    handleUsernameChanged(user) {
        this.setState({
            user: user
        });
    }

    /**
     * handles lunchtime selection; sets result for display component
     */
    handleCoffeeLunchOptionSelected(opt) {
        const ctx = this;
        if (["lunch", "coffee"].indexOf(opt) > -1) {
            axios
                .post(
                    '/lunchtime',
                    {
                        meetup_type: opt,
                        user: ctx.state.user
                    }
                )
                .then(function(res) {
                    ctx.setState({
                        userActionResult: res.data.result
                    });
                });
        }
    }

    isUsernameValid() {
        return this.state.user.length > 0;
    }

    render() {
        return (
            <AppContainerCard>
                {this.state.userAdded 
                    ?
                        <LunchCoffeeForm
                            result={this.state.userActionResult}
                            onOptionSelected={this.handleCoffeeLunchOptionSelected}
                        />
                    :
                        <UserForm
                            onUserSet={this.handleUserSet}
                            checkUsernameValid={this.isUsernameValid}
                            onUsernameChanged={this.handleUsernameChanged}
                        />
                }
            </AppContainerCard>
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
