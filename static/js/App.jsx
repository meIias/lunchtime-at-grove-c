/**
 * App.jsx
 *
 * - react app container, conditionally loads ui views
 */

import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import UserForm from './UserForm.jsx';
import LunchCoffeeForm from './LunchCoffeeForm.jsx';
import AppContainerCard from "./AppContainerCard.jsx";

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: "",
            userAdded: false
        };
        this.handleUserSet = this.handleUserSet.bind(this);
        this.handleUsernameChanged = this.handleUsernameChanged.bind(this);
        this.handleCoffeeLunchOptionSelected = this.handleCoffeeLunchOptionSelected.bind(this);
    }

    handleUserSet() {
        this.setState({
            userAdded: true
        });
    }

    handleUsernameChanged(user) {
        this.setState({
            user: user
        });
    }

    handleCoffeeLunchOptionSelected(opt) {
        if (opt === 'lunch') {
        } else if (opt === 'coffee') {
        }
    }

    render() {
        return (
            <AppContainerCard>
                {this.state.userAdded 
                    ?
                        <LunchCoffeeForm
                            result={"TODO"}
                            onOptionSelected={this.handleCoffeeLunchOptionSelected}
                        />
                    :
                        <UserForm
                            onUserSet={this.handleUserSet}
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
