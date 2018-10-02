/**
 * UserForm.jsx
 *
 * - contains the user input ui
 */

import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledInput = styled.input`
    font-size:18px;
    padding:10px 10px 10px 5px;
    display:block;
    width:300px;
    border:none;
    border-bottom:1px solid #757575;
`;

const StyledDiv = styled.div`
    display: inline-block;
`;

const StyledLabel = styled.div`
    color: #a1a1a1;
    font-size: 24px;
    margin-right: 12px;
    text-transform: uppercase;
    font-family: 'Roboto', sans-serif;
`;

const StyledButton = styled.button`
    padding: 8px;
    cursor: pointer;
    margin-left: 12px;

    font-size:18px;
    text-transform: uppercase;
    font-family: 'Roboto', sans-serif;
`;

/**
 * UserForm - Component
 *
 * - renders username input field
 * - displayed before getting lunch/coffee options
 */
const UserForm = props => (
    <div>
        <StyledDiv>
            <StyledLabel>
                User
            </StyledLabel>
        </StyledDiv>
        <StyledDiv>
            <StyledInput
                type="text"
                onChange={ev => props.onUsernameChanged(ev.target.value)}
            />
        </StyledDiv>
        <StyledDiv>
            <StyledButton
                onClick={props.onUserSet}
            >
                GO
            </StyledButton>
        </StyledDiv>
    </div>
);

UserForm.propTypes = {
    onUserSet: PropTypes.func.isRequired,
    onUsernameChanged: PropTypes.func.isRequired
};

export default UserForm;
