<template>
    <div>
        <h1>Чат на vue js</h1>
        <button v-if="!auth" @click="goLogin">Вход</button>
        <button v-else @click="logout">Выход</button>
        <Room v-if="auth"></Room>
    </div>
</template>

<script>
    import Room from "./Room";

    export default {
        name: "Home",
        components: {Room},
        comments: {
            Room,
        },
        computed: {         // вычисляемые свойства
            auth() {    // проверка авторизции пользователя
                if (sessionStorage.getItem("auth_token")) {
                    // проверка sessionStorageStorage и взятие токена, если он существует
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")         // выход
                window.location = '/'           // костыльный вариант
            }
        }

    }
</script>

<style scoped>

</style>
