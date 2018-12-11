import React, { Component } from 'react';
import { connect } from 'react-redux';
import { FormGroup, FormControl, Button } from 'react-bootstrap';
import { search } from '../actions/searchengine';

const mapStateToProps = state => ({
    loading: state.search.fetching,
  })

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
        const { value } = this.state
        const { dispatch } = this.props;
        
        if (value !== '') {
            dispatch(search(value));
        }
    }

  render() {
      const { loading } = this.props;
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

        <Button bsStyle="primary" type="button" onClick={this.handleSubmit} disabled={loading}>
            {loading ? 'Loading...' : 'Search'}
        </Button>
    </form>
    );
  }
}

export default connect(mapStateToProps)(SearchForm);
