<template>
    <div>
        <h1>Чат на vue js</h1>
        <button v-if="!auth" @click="goLogin">Вход</button>
        <button v-else @click="logout">Выход</button>

        <room v-if="auth" @openDialog="openDialog"></room>
        <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </div>
</template>

<script>
    import Room from "./Rooms/Room.vue";
    import Dialog from "./Rooms/Dialog.vue";

    export default {
        name: "Home",
        components: {
            Room,
            Dialog
        },
        data() {        // хранение списка наших комнат
            return {
                dialog: {
                    id: '',
                    show: false,
                }
            }
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
            },
            openDialog(id) {
                this.dialog.id = id
                this.dialog.show = true
            }
        }
    }
</script>

<style scoped>

</style>
