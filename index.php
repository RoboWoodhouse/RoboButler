<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Header -->
    <?php include ('content/header.php'); ?>
  </head>

  <body>
  <nav  class="navbar navbar-inverse">
    <?php include ('content/navbar.php'); ?>
  </nav>

  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12 main">
        <center>
        <h1 class="page-header">Dashboard</h1>
        </center>
      </div><!--Page Header-->
    </div><!-- row-->
    <div class="row">
      <?php include ('content/activity.php'); ?>
    </div><!--row-->
    <div class="row">
      <?php include ('content/bvg.php'); ?>
    </div><!-- row-->
  </div><!-- container -->
  </body>
</html>
