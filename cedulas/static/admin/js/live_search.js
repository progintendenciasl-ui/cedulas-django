document.addEventListener("DOMContentLoaded", function () {

    const input = document.querySelector("#searchbar");

    if (input) {

        let timeout = null;

        input.addEventListener("input", function () {

            clearTimeout(timeout);

            timeout = setTimeout(function () {

                const value = input.value;

                const url = new URL(window.location.href);

                if (value.trim() !== "") {
                    url.searchParams.set("q", value);
                } else {
                    url.searchParams.delete("q");
                }

                window.location.href = url.toString();

            }, 1000);

        });

    }

});