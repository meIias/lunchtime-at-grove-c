/**
 * AppContainerCard.jsx
 *
 * - contains the component displaying a bordered div around the inner forms
 */

import React from 'react';
import styled from 'styled-components';

const CONTAINER_FRAME_COLOR = "#9BC35C";

const AppContainerCardContainer = styled.div`
    width: 450px;
    height: 210px;
    border-radius: 8px;
    border: 2px solid #cfcfcf;

    box-shadow: 1px 1px 9px 1px rgba(161,161,161,1);
    -moz-box-shadow: 1px 1px 9px 1px rgba(161,161,161,1);
    -webkit-box-shadow: 1px 1px 9px 1px rgba(161,161,161,1);
`;

const AppContainerCardFrame = styled.div`
    width: 444px;
    height: 204px;
    border-radius: 6px;
    background-color: white;
    border: 3px solid ${CONTAINER_FRAME_COLOR};

    display: flex;
    align-items: center;
    justify-content: center;
`;

/**
 * AppContainerCard - Component
 *
 * - displays a framed border around input
 */
const AppContainerCard = props => (
    <AppContainerCardContainer> 
        <AppContainerCardFrame>
            {props.children}
        </AppContainerCardFrame> 
    </AppContainerCardContainer> 
);

export default AppContainerCard;
