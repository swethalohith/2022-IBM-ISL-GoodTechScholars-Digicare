<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Digicare</title>
	<link rel="stylesheet" href="static/fontawesome/css/all.min.css"> <!-- https://fontawesome.com/ -->
	<link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap" rel="stylesheet"> <!-- https://fonts.google.com/ -->
    <!--<link href="css/bootstrap.min.css" rel="stylesheet">-->
    <link href="static/css/digicare.css" rel="stylesheet">

</head>
<body>
	<header class="tm-header" id="tm-header">
        <div class="tm-header-wrapper">
            <button class="navbar-toggler" type="button" aria-label="Toggle navigation">
                <i class="fas fa-bars"></i>
            </button>
            <div class="tm-site-header">
              <!--  <div class="mb-3 mx-auto tm-site-logo"><i class="fas fa-times fa-2x"></i>
                    <img src="static/img/Logo_white.png" >
                </div>-->
                <img src="static/img/Logo_white.png" width = '300' height='300' />
                <h2 class="text-center">Digicare</h2>
            </div>
            <nav class="tm-nav" id="tm-nav">
                <ul>
                    <li class="tm-nav-item "><a href="templates/index.html" class="tm-nav-link">
                        <i class="fas fa-home"></i>
                        Personal Details
                    </a></li>
                    <li class="tm-nav-item active"><a href="templates/medicaldetails.html" class="tm-nav-link">
                        <i class="fas fa-pen"></i>
                        Medical Details
                    </a></li>
                    <li class="tm-nav-item"><a href="templates/medicalhistory.html" class="tm-nav-link">
                        <i class="fas fa-users"></i>
                        Medical History
                    </a></li>
                    <li class="tm-nav-item"><a href="templates/login.html" class="tm-nav-link">
                        <i class="fas fa-users"></i>
                        Log Out
                    </a></li>
                    <!--<li class="tm-nav-item"><a href="templates/contact.html" class="tm-nav-link">
                        <i class="far fa-comments"></i>
                        Contact Us
                    </a></li>-->
                </ul>
            </nav>

            <h4 class="tm-mb-80 pr-5 text-white">
                DIGICARE
            </h4>
        </div>
    </header>
    <div class="container-fluid">
        <main class="tm-main">
            <!-- Search form -->

            <div class="row tm-row">
                <article class="col-12 col-md-6 tm-post">

                        <h2 class="tm-pt-30 tm-color-primary tm-post-title">Basic Details</h2>
                        <!--<font size=5><font color: #999>-->
                    <p class="tm-pt-30">
                            Blood Group&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;AB+<br>
                            Height&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;179 cm<br>
                            Weight&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;74 kg<br>
                    </p>
                    <hr>
                    <h2 class="tm-pt-30 tm-color-primary tm-post-title">Allergies</h2>
                        <!--<font size=5><font color: #999>-->

                    <p class="tm-pt-30">
                            Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Eczema<br>
                            Adverse Reactions&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Rashes,Itching<br>
                            Immunization&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Dupilumab<br>
                            Drug Allergies&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Sulpha drugs<br>
                            Allergens&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Peanut,Pollen<br>
                    </p>
                    <hr>
                    <h2 class="tm-pt-30 tm-color-primary tm-post-title">Ongoing Medication</h2>
                    <!--<font size=5><font color: #999>-->

                    <p class="tm-pt-30">
                        Disease&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Cerebral Venous Thrombosis<br>
                        Medicine Taken&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Heparin<br>
                        Dosage&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;20 units/hour<br>
                        Duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;3 months<br>
                        Date&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;19/04/2022<br>
                    </p>
                    <hr>
                    <h2 class="tm-pt-30 tm-color-primary tm-post-title">Consulting Doctor</h2>
                    <!--<font size=5><font color: #999>-->

                    <p class="tm-pt-30">
                        Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Dr Mary Philip<br>
                        Hospital&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Trinity Hospital,Hsuty<br>
                        Email ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;mary@gmail.com<br>
                   </p>
                  <hr>
                  <h2 class="tm-pt-30 tm-color-primary tm-post-title">Remarks</h2>
                  <!--<font size=5><font color: #999>-->
                  <p class="tm-pt-30">
                      Check up after 3 months&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;Nil<br>

                    </p>

            </div>
        </main>
    </div>

</body>
</html>
