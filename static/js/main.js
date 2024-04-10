<script>
    $(document).ready(function() {
        $('#user-profile a').click(function(event) {
            event.preventDefault();
            window.location.href = $(this).attr('href');
        })
    });
</script>