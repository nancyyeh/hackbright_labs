"use strict";

class Homepage extends React.Component {
  render() {
    return (
      <div>
        <p>Welcome message</p>
        <a href="/cards">Click here to view the trading cards</a><br></br>
        <img src="/static/img/balloonicorn.jpg" alt=""/>
      </div>
    );
  }
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));
