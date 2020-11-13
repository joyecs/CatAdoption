import React from "react";
import { Link } from "react-router-dom";

// const active_tab = () => {}

function TopNav() {
    return (
        <div id="header-wrapper">
            <header id="header" className="container">
                <div id="logo">
                    <h1><Link to="/">Kitty</Link></h1>
                    <span>House</span>
                </div>

                <nav id="nav">
                    <ul>
                        <li> 
                            <Link to="/" className={window.location.pathname === "/" ? "current" : ""}>Welcome</Link>         
                        </li>
                        <li>
                            <Link to="/adopt" className={window.location.pathname === "/adopt" ? "current" : ""}>Adopt</Link>
                        </li>
                        <li>
                            <Link to="/donate" className={window.location.pathname === "/donate" ? "current" : ""}>Donate</Link>
                        </li>
                        <li>
                            <Link to="/volunteer" className={window.location.pathname === "/volunteer" ? "current" : ""}>Volunteer</Link>
                        </li>
                    </ul>
                </nav>
            </header>
        </div>
    );
}

export default TopNav;