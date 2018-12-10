import React, { Component } from 'react';
import { connect } from 'react-redux';
import { FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';
import { USER_BASED_EUCLIDEAN, USER_BASED_PEARSON, ITEM_BASED_EUCLIDEAN } from '../constants/actionTypes';
import { fetchUserBasedRec, fetchItemBasedRec } from '../actions/recommendations';

class SearchForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: ''
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        this.setState({ value: e.target.value });
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
        <FormGroup
          controlId="formBasicText"
        >
          <FormControl
            type="text"
            value={this.state.value}
            placeholder="Enter text"
            onChange={this.handleChange}
          />
          <FormControl.Feedback />
        </FormGroup>

        <Button bsStyle="primary" type="button" onClick={this.handleSubmit}>Search</Button>
    </form>
    );
  }
}

export default connect()(SearchForm);
