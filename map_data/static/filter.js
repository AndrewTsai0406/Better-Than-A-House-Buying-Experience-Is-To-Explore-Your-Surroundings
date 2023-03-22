<!--PRICE RANGE SLIDER script-->
  <script type="text/javascript">
    (function ($) {

      $('#price-range-submit').hide();

      $("#min_price,#max_price").on('change', function () {

        $('#price-range-submit').show();

        var min_price_range = parseInt($("#min_price").val());

        var max_price_range = parseInt($("#max_price").val());

        if (min_price_range > max_price_range) {
          $('#max_price').val(min_price_range);
        }

        $("#slider-range").slider({
          values: [min_price_range, max_price_range]
        });

      });


      $("#min_price,#max_price").on("paste keyup", function () {                                        

        $('#price-range-submit').show();

        var min_price_range = parseInt($("#min_price").val());

        var max_price_range = parseInt($("#max_price").val());

        if(min_price_range == max_price_range){

          max_price_range = min_price_range + 500;

          $("#min_price").val(min_price_range);   
          $("#max_price").val(max_price_range);
        }

        $("#slider-range").slider({
          values: [min_price_range, max_price_range]
        });

      });


      $(function () {
        $("#slider-range").slider({
          range: true,
          orientation: "horizontal",
          min: 0,
          max: 10000,
          values: [0, 10000],
          step: 500,

          slide: function (event, ui) {
            if (ui.values[0] == ui.values[1]) {
              return false;
            }

            $("#min_price").val(ui.values[0]);
            $("#max_price").val(ui.values[1]);
          }
        });

        $("#min_price").val($("#slider-range").slider("values", 0));
        $("#max_price").val($("#slider-range").slider("values", 1));

      });

        /*$("#slider-range,#price-range-submit").click(function () {

          var min_price = $('#min_price').val();
          var max_price = $('#max_price').val();

          $("#searchResults").text("Here List of houses will be shown which are cost between " + min_price  +" "+ "and" + " "+ max_price + ".");
        });*/


      });
    </script>

    <!--AGE of HOUSE RANGE SLIDER script-->
    <script type="text/javascript">
      (function ($) {

        $('#age-range-submit').hide();

        $("#min_age,#max_age").on('change', function () {

          $('#age-range-submit').show();

          var min_age_range = parseInt($("#min_age").val());

          var max_age_range = parseInt($("#max_age").val());

          if (min_age_range > max_age_range) {
            $('#max_age').val(min_age_range);
          }

          $("#slider-age-range").slider({
            values: [min_age_range, max_age_range]
          });

        });


        $("#min_age,#max_age").on("paste keyup", function () {                                        

          $('#age-range-submit').show();

          var min_age_range = parseInt($("#min_age").val());

          var max_age_range = parseInt($("#max_age").val());

          if(min_age_range == max_age_range){

            max_age_range = min_age_range + 5;

            $("#min_age").val(min_age_range);   
            $("#max_age").val(max_age_range);
          }

          $("#slider-age-range").slider({
            values: [min_age_range, max_age_range]
          });

        });


        $(function () {
          $("#slider-age-range").slider({
            range: true,
            orientation: "horizontal",
            min: 0,
            max: 60,
            values: [0, 60],
            step: 5,

            slide: function (event, ui) {
              if (ui.values[0] == ui.values[1]) {
                return false;
              }

              $("#min_age").val(ui.values[0]);
              $("#max_age").val(ui.values[1]);
            }
          });

          $("#min_age").val($("#slider-age-range").slider("values", 0));
          $("#max_age").val($("#slider-age-range").slider("values", 1));

        });

      });
    </script>

    <!--FLOOR NO. RANGE SLIDER script-->
    <script type="text/javascript">
      (function ($) {

        $('#floornb-range-submit').hide();

        $("#min_floornb,#max_floornb").on('change', function () {

          $('#floornb-range-submit').show();

          var min_floornb_range = parseInt($("#min_floornb").val());

          var max_floornb_range = parseInt($("#max_floornb").val());

          if (min_floornb_range > max_floornb_range) {
            $('#max_floornb').val(min_floornb_range);
          }

          $("#slider-floornb-range").slider({
            values: [min_floornb_range, max_floornb_range]
          });

        });


        $("#min_floornb,#max_floornb").on("paste keyup", function () {                                        

          $('#floornb-range-submit').show();

          var min_floornb_range = parseInt($("#min_floornb").val());

          var max_floornb_range = parseInt($("#max_floornb").val());

          if(min_floornb_range == max_floornb_range){

            max_floornb_range = min_floornb_range + 1;

            $("#min_floornb").val(min_floornb_range);   
            $("#max_floornb").val(max_floornb_range);
          }

          $("#slider-floornb-range").slider({
            values: [min_floornb_range, max_floornb_range]
          });

        });


        $(function () {
          $("#slider-floornb-range").slider({
            range: true,
            orientation: "horizontal",
            min: 0,
            max: 50,
            values: [0, 50],
            step: 1,

            slide: function (event, ui) {
              if (ui.values[0] == ui.values[1]) {
                return false;
              }

              $("#min_floornb").val(ui.values[0]);
              $("#max_floornb").val(ui.values[1]);
            }
          });

          $("#min_floornb").val($("#slider-floornb-range").slider("values", 0));
          $("#max_floornb").val($("#slider-floornb-range").slider("values", 1));

        });

      });
    </script>

    <!--TOTAL FLOORS RANGE SLIDER script-->
    <script type="text/javascript">
      (function ($) {

        $('#total-fl-range-submit').hide();

        $("#min_total_fl,#max_total_fl").on('change', function () {

          $('#total-fl-range-submit').show();

          var min_total_fl_range = parseInt($("#min_total_fl").val());

          var max_total_fl_range = parseInt($("#max_total_fl").val());

          if (min_total_fl_range > max_total_fl_range) {
            $('#max_total_fl').val(min_total_fl_range);
          }

          $("#slider-total-fl-range").slider({
            values: [min_total_fl_range, max_total_fl_range]
          });

        });


        $("#min_total_fl,#max_total_fl").on("paste keyup", function () {                                        

          $('#total-fl-range-submit').show();

          var min_total_fl_range = parseInt($("#min_total_fl").val());

          var max_total_fl_range = parseInt($("#max_total_fl").val());

          if(min_total_fl_range == max_total_fl_range){

            max_total_fl_range = min_total_fl_range + 1;

            $("#min_total_fl").val(min_total_fl_range);   
            $("#max_total_fl").val(max_total_fl_range);
          }

          $("#slider-total-fl-range").slider({
            values: [min_total_fl_range, max_total_fl_range]
          });

        });


        $(function () {
          $("#slider-total-fl-range").slider({
            range: true,
            orientation: "horizontal",
            min: 0,
            max: 15,
            values: [0, 15],
            step: 1,

            slide: function (event, ui) {
              if (ui.values[0] == ui.values[1]) {
                return false;
              }

              $("#min_total_fl").val(ui.values[0]);
              $("#max_total_fl").val(ui.values[1]);
            }
          });

          $("#min_total_fl").val($("#slider-total-fl-range").slider("values", 0));
          $("#max_total_fl").val($("#slider-total-fl-range").slider("values", 1));

        });

      });
    </script>