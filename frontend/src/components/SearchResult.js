import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Table } from 'react-bootstrap';

const mapStateToProps = state => ({
  searchResult: state.search.result,
})

class SearchResult extends Component {

  render() {
    const { searchResult } = this.props;

    return searchResult.length > 0 ? (
    <Table striped bordered condensed hover>
    <thead>
        <tr>
        <th>Name</th>
        <th>Score</th>
        <th>Content</th>
        <th>Location</th>
        <th>PageRank</th>
        </tr>
    </thead>
    <tbody>
        {searchResult.map((score, key) => 
                <tr>
                    <td>
                      <a
                        href={`http://wikipedia.org/${score.link}`}
                        style={{float: 'left'}}
                      >
                      {decodeURIComponent(score.link.split('/')[2].replace(/\+/g, ' '))}
                      </a></td>
                    <td>{Math.round(score.score * 100) / 100}</td>
                    <td>{Math.round(score.frequency * 100) / 100}</td>
                    <td>{Math.round(score.location * 100) / 100}</td>
                    <td>{Math.round(score.pageRank * 100) / 100}</td>
                </tr>
            )}
    </tbody>
    </Table>
    ) : <div></div>;
  }
}

export default connect(mapStateToProps)(SearchResult);
