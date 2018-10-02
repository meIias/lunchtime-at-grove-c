/**
 *
 * LunchCoffeeForm.jsx
 *
 * - contains the component for lunch/coffee buttons and results
 */

import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const FlexContainerDiv = styled.div`
    width: 100%;
    height: 100%;

    display: flex;
    flex-wrap: wrap;
`;

const FlexButtonDiv = styled.div`
    width: 50%;
    text-align: center;
`;

const FlexResultStringDiv = styled.div`
    width: 100%;
`;

const StyledButton = styled.button`
    width: 100%;
    height: 50%;
    padding 24px;
    cursor: pointer;

    font-size:18px;
    text-transform: uppercase;
    font-family: 'Roboto', sans-serif;
`;

const StyledTextContainer = styled.div`
    padding: 24px;
    text-align: center;

    font-size:18px;
    font-family: 'Roboto', sans-serif;
`;

/**
 * LunchCoffeeForm - Component
 *
 * - displays lunch/coffee choices as well as result upon selection
 */
const LunchCoffeeForm = props => (
    <FlexContainerDiv>
        <FlexButtonDiv>
            <StyledButton
                onClick={() => props.onOptionSelected('coffee')}
            >
                Lets get coffee!
            </StyledButton>
        </FlexButtonDiv>
        <FlexButtonDiv>
            <StyledButton
                onClick={() => props.onOptionSelected('lunch')}
            >
                Lets get lunch!
            </StyledButton>
        </FlexButtonDiv>
        <FlexResultStringDiv>
            <StyledTextContainer>
                {props.result}
            </StyledTextContainer>
        </FlexResultStringDiv>
    </FlexContainerDiv>
);

LunchCoffeeForm.propTypes = {
    result: PropTypes.string.isRequired,
    onOptionSelected: PropTypes.func.isRequired
};

LunchCoffeeForm.defaultProps = {
    result: ""
};

export default LunchCoffeeForm;
