import React, { Component } from 'react';
import { connect } from 'react-redux';
import { FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';
import { USER_BASED_EUCLIDEAN, USER_BASED_PEARSON, ITEM_BASED_EUCLIDEAN } from '../constants/actionTypes';
import { recMethods } from '../constants/environment';
import { fetchUserBasedRec, fetchItemBasedRec } from '../actions/recommendations';

class RecommendationSelector extends Component {

    constructor(props) {
        super(props);
        this.state = {
            collMethod: null,
            algorithm: null,
        }

        this.handleCollChange = this.handleCollChange.bind(this);
        this.handleAlgChange = this.handleAlgChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleCollChange(e) {
        this.setState({ collMethod: e.target.value });
    }

    handleAlgChange(e) {
        this.setState({ algorithm: e.target.value });
    }

    handleSubmit(e) {
        const { user, dispatch } = this.props;
        
        if (this.state.collMethod === 'user-based') {
            if (this.state.algorithm === 'euclidean') {
                dispatch(fetchUserBasedRec(user, USER_BASED_EUCLIDEAN));
            } else if (this.state.algorithm === 'pearson') {
                dispatch(fetchUserBasedRec(user, USER_BASED_PEARSON));
            }
        } else if (this.state.collMethod === 'item-based') {
            if (this.state.algorithm === 'euclidean') {
                dispatch(fetchItemBasedRec(user, ITEM_BASED_EUCLIDEAN));
            }
        }
    }

  render() {
    return (
        <form style={{ 'margin-top': '50px'}}>
        <ControlLabel>User-based or Item-based</ControlLabel>
        <FormGroup controlId="collMethod">
            <FormControl componentClass="select" placeholder="select" onChange={this.handleCollChange}>
                <option value="select">select</option>
                {Object.keys(recMethods).map((key, id) => <option key={id} value={key}>{key}</option> )}
            </FormControl>
        </FormGroup>

        <ControlLabel>Algorithm</ControlLabel>
        <FormGroup controlId="algorithm">
            <FormControl componentClass="select" placeholder="select" onChange={this.handleAlgChange}>
                <option value="select">select</option>
                {this.state.collMethod && recMethods[this.state.collMethod].map((val, id) => 
                    <option key={id} value={val}>{val}</option>
                    )}
            </FormControl>
        </FormGroup>

        <Button bsStyle="primary" type="button" onClick={this.handleSubmit}>Submit</Button>
    </form>
    );
  }
}

export default connect()(RecommendationSelector);
