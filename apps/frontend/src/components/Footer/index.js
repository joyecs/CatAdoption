import React from "react";

function Footer() {
    return (
        <div id="footer-wrapper">
            <footer id="footer" className="container">
                <div className="row">
                    <div className="col-6 col-6-medium col-12-small">

                        <section className="widget links">
                            <h3>Quick Link</h3>
                            <ul className="style2">
                                <li><a href="./adopt.html">Adopt</a></li>
                                <li><a href="./donate.html">Donate</a></li>
                                <li><a href="./volunteer.html">Volunteer</a></li>
                            </ul>
                        </section>
                    </div>

                    <div classNameName="col-6 col-6-medium col-12-small">

                        <section className="widget contact">
                            <h3>Contact Us</h3>
                            <ul>
                                <li><a href="#" className="icon brands fa-twitter"><span className="label">Twitter</span></a>
                                </li>
                                <li><a href="#" className="icon brands fa-facebook-f"><span
                                    className="label">Facebook</span></a></li>
                                <li><a href="#" className="icon brands fa-instagram"><span
                                    className="label">Instagram</span></a></li>
                                <li><a href="#" className="icon brands fa-dribbble"><span className="label">Dribbble</span></a>
                                </li>
                                <li><a href="#" className="icon brands fa-pinterest"><span
                                    className="label">Pinterest</span></a></li>
                            </ul>
                            <p>14736 Valley Blvd,
                            La Puente, CA.
								Kitty House</p>
                        </section>

                    </div>
                </div>
                <div className="row">
                    <div className="col-12">
                        <div id="copyright">
                            <ul className="menu">
                                <li>COPYRIGHT © 2020, PIKICODE CORP. ALL RIGHTS RESERVED.C4039862</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
};

export default Footer;