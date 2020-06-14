<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'App',
        // если храним token в localStorage
        // created() {                      // при загрузки точки входа в нашее приложение
        //     if (localStorage.getItem("auth_token")) {       // проверка localStorage и взятие токена, если он существует
        //         $.ajaxSetup({                //  в ajaxSetup занесим в headers
        //             headers: {'Authorization': "Token " + localStorage.getItem('auth_token')},
        //             // "Authorization": "Token 6a57d9af66fcf68b9fac066e67d4a450f5cf667a"
        //         });
        //     }
        // }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
