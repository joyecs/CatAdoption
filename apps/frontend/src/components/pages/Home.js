import React from "react";

function Home() {
    return (
        <div>
            <div id="banner-wrapper">
                <div id="banner" className="box container">
                    <div className="row">
                        <div className="col-7 col-12-medium">
                            <h3>Hi. This is Kitty House.</h3>
                            <p>We urgently need kitten adopters. Ready to get started?</p>
                        </div>
                        <div className="col-5 col-12-medium">
                            <ul>
                                <li><a href="adopt.html" className="button large icon solid fa-arrow-circle-right">Ok let's go</a></li>
                                <li><a href="volunteer.html" className="button alt large icon solid fa-question-circle">More info</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div id="features-wrapper">
                <div className="container">
                    <div className="row">
                        <div className="col-4 col-12-medium">

                            <section className="box feature">
                                <a className="image featured"><img src="images/kitty01.jpeg" alt="" className="img-index" /></a>
                                <div className="inner">
                                    <header>
                                        <h2>Kitten is not just cute!</h2>
                                        <p>We encourage everyone to adopt one.</p>
                                    </header>
                                    <p>
                                        You can get all the food and litter from us if you like!
											</p>
                                </div>
                            </section>

                        </div>
                        <div className="col-4 col-12-medium">
                            <section className="box feature">
                                <a className="image featured"><img src="images/kitty02.jpeg" alt="" className="img-index" /></a>
                                <div className="inner">
                                    <header>
                                        <h2>You get company!</h2>
                                        <p>Social distancing is better with a cat. </p>
                                    </header>
                                    <p>
                                        When you find kittens outside, it's natural to be concerned.
											</p>
                                </div>
                            </section>

                        </div>
                        <div className="col-4 col-12-medium">

                            <section className="box feature">
                                <a className="image featured"><img src="images/kitty03.jpeg" alt="" className="img-index" /></a>
                                <div className="inner">
                                    <header>
                                        <h2>Love, care and attention!</h2>
                                        <p>With a little effort, you can save a life!</p>
                                    </header>
                                    <p>
                                        Isn't it cute and warm to have a cat around you?
											</p>
                                </div>
                            </section>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Home;