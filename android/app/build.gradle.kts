import java.util.Properties

plugins {
    id("com.android.application")
}

// The release key lives outside the repo. Point KEYSTORE_PROPERTIES at a file with
// storeFile, storePassword, keyAlias and keyPassword, or leave it unset for a debug build.
val keystoreProps = Properties().apply {
    val path = System.getenv("KEYSTORE_PROPERTIES") ?: "C:/Users/GM/Documents/live-quiz-keys/keystore.properties"
    val f = file(path)
    if (f.exists()) f.inputStream().use { load(it) }
}

android {
    namespace = "uk.letsquiz.tv"
    compileSdk = 36

    defaultConfig {
        applicationId = "uk.letsquiz.tv"
        minSdk = 22          // Fire OS 5 (Fire TV Stick 1st gen) and up
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"
    }

    signingConfigs {
        if (keystoreProps.getProperty("storeFile") != null) {
            create("release") {
                storeFile = file(keystoreProps.getProperty("storeFile"))
                storePassword = keystoreProps.getProperty("storePassword")
                keyAlias = keystoreProps.getProperty("keyAlias")
                keyPassword = keystoreProps.getProperty("keyPassword")
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            signingConfig = signingConfigs.findByName("release") ?: signingConfigs.getByName("debug")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}
