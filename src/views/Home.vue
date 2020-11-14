<template>
  <div style="height: 100%;">
    <v-toolbar :dark="isDark">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-tooltip bottom>
        <template data-app v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon @click="changeTheme">
            <v-icon>mdi-invert-colors</v-icon>
          </v-btn>
        </template>
        <span>Change theme</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template data-app v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon @click="openSource">
            <v-icon>mdi-github</v-icon>
          </v-btn>
        </template>
        <span>View source</span>
      </v-tooltip>
    </v-toolbar>
    <Particles :key="particlesKey" id="tsparticles"
      :options='{
  "autoPlay": true,
  "background": {
    "color": {
      "value": isDark ? "#000000" : "#cccccc"
    },
    "image": "",
    "position": "",
    "repeat": "",
    "size": "",
    "opacity": 1
  },
  "backgroundMask": {
    "composite": "destination-out",
    "cover": {
      "color": {
        "value": "#000000"
      },
      "opacity": 1
    },
    "enable": false
  },
  "backgroundMode": {
    "enable": false,
    "zIndex": -1
  },
  "detectRetina": true,
  "fpsLimit": 60,
  "infection": {
    "cure": false,
    "delay": 0,
    "enable": false,
    "infections": 0,
    "stages": []
  },
  "interactivity": {
    "detectsOn": "window",
    "events": {
      "onClick": {
        "enable": true,
        "mode": "push"
      },
      "onDiv": {
        "selectors": [],
        "enable": false,
        "mode": [],
        "type": "circle"
      },
      "onHover": {
        "enable": true,
        "mode": "grab",
        "parallax": {
          "enable": true,
          "force": -30,
          "smooth": 30
        }
      },
      "resize": true
    },
    "modes": {
      "attract": {
        "distance": 200,
        "duration": 0.4,
        "speed": 1
      },
      "bounce": {
        "distance": 200
      },
      "bubble": {
        "distance": 200,
        "duration": 0.4
      },
      "connect": {
        "distance": 80,
        "links": {
          "opacity": 0.5
        },
        "radius": 60
      },
      "grab": {
        "distance": 100,
        "links": {
          "blink": false,
          "consent": false,
          "opacity": 1
        }
      },
      "light": {
        "area": {
          "gradient": {
            "start": {
              "value": "#000000"
            },
            "stop": {
              "value": "#000000"
            }
          },
          "radius": 1000
        },
        "shadow": {
          "color": {
            "value": "#000000"
          },
          "length": 2000
        }
      },
      "push": {
        "quantity": 4
      },
      "remove": {
        "quantity": 2
      },
      "repulse": {
        "distance": 200,
        "duration": 0.4,
        "speed": 1
      },
      "slow": {
        "factor": 3,
        "radius": 200
      },
      "trail": {
        "delay": 0.005,
        "quantity": 5,
        "particles": {
          "color": {
            "value": "#ff0000",
            "animation": {
              "enable": true,
              "speed": 400,
              "sync": true
            }
          },
          "collisions": {
            "enable": false,
            "bounce": {
              "horizontal": {
                "random": {}
              },
              "vertical": {
                "random": {}
              }
            }
          },
          "links": {
            "enable": false,
            "shadow": {},
            "triangles": {}
          },
          "move": {
            "outMode": "destroy",
            "speed": 5,
            "angle": {},
            "attract": {
              "rotate": {}
            },
            "gravity": {},
            "noise": {
              "delay": {
                "random": {}
              }
            },
            "outModes": {},
            "trail": {}
          },
          "size": {
            "value": 5,
            "animation": {
              "enable": true,
              "speed": 5,
              "minimumValue": 1,
              "sync": true,
              "startValue": "min",
              "destroy": "max"
            },
            "random": {}
          },
          "bounce": {
            "horizontal": {
              "random": {}
            },
            "vertical": {
              "random": {}
            }
          },
          "life": {
            "delay": {
              "random": {}
            },
            "duration": {
              "random": {}
            }
          },
          "number": {
            "density": {}
          },
          "opacity": {
            "animation": {},
            "random": {}
          },
          "rotate": {
            "animation": {}
          },
          "shadow": {
            "offset": {}
          },
          "shape": {},
          "stroke": {
            "color": {
              "value": "",
              "animation": {
                "enable": false,
                "speed": 0,
                "sync": false
              }
            }
          },
          "twinkle": {
            "lines": {},
            "particles": {}
          }
        }
      }
    }
  },
  "manualParticles": [],
  "motion": {
    "disable": false,
    "reduce": {
      "factor": 4,
      "value": true
    }
  },
  "particles": {
    "bounce": {
      "horizontal": {
        "random": {
          "enable": false,
          "minimumValue": 0.1
        },
        "value": 1
      },
      "vertical": {
        "random": {
          "enable": false,
          "minimumValue": 0.1
        },
        "value": 1
      }
    },
    "collisions": {
      "bounce": {
        "horizontal": {
          "random": {
            "enable": false,
            "minimumValue": 0.1
          },
          "value": 1
        },
        "vertical": {
          "random": {
            "enable": false,
            "minimumValue": 0.1
          },
          "value": 1
        }
      },
      "enable": true,
      "mode": "bounce"
    },
    "color": {
      "value": "#f00",
      "animation": {
        "enable": true,
        "speed": 50,
        "sync": false
      }
    },
    "life": {
      "count": 0,
      "delay": {
        "random": {
          "enable": false,
          "minimumValue": 0
        },
        "value": 0,
        "sync": false
      },
      "duration": {
        "random": {
          "enable": false,
          "minimumValue": 0.0001
        },
        "value": 0,
        "sync": false
      }
    },
    "links": {
      "blink": false,
      "color": {
        "value": "random"
      },
      "consent": false,
      "distance": 100,
      "enable": true,
      "frequency": 1,
      "opacity": 1,
      "shadow": {
        "blur": false,
        "color": {
          "value": "#00ff00"
        },
        "enable": false
      },
      "triangles": {
        "enable": false,
        "frequency": 1
      },
      "width": 1,
      "warp": false
    },
    "move": {
      "angle": {
        "offset": 45,
        "value": 90
      },
      "attract": {
        "enable": false,
        "rotate": {
          "x": 3000,
          "y": 3000
        }
      },
      "direction": "none",
      "distance": 0,
      "enable": true,
      "gravity": {
        "acceleration": 9.81,
        "enable": false,
        "maxSpeed": 50
      },
      "noise": {
        "delay": {
          "random": {
            "enable": false,
            "minimumValue": 0
          },
          "value": 0
        },
        "enable": false
      },
      "outModes": {
        "default": "out"
      },
      "random": false,
      "size": false,
      "speed": 2,
      "straight": false,
      "trail": {
        "enable": false,
        "length": 10,
        "fillColor": {
          "value": "#000000"
        }
      },
      "vibrate": false,
      "warp": false
    },
    "number": {
      "density": {
        "enable": true,
        "area": 800,
        "factor": 1000
      },
      "limit": 0,
      "value": 100
    },
    "opacity": {
      "random": {
        "enable": true,
        "minimumValue": 0.3
      },
      "value": 0.8,
      "animation": {
        "enable": true,
        "minimumValue": 0.3,
        "speed": 0.5,
        "sync": false
      }
    },
    "reduceDuplicates": false,
    "rotate": {
      "random": {
        "enable": false,
        "minimumValue": 0
      },
      "value": 0,
      "animation": {
        "enable": false,
        "speed": 0,
        "sync": false
      },
      "direction": "clockwise",
      "path": false
    },
    "shadow": {
      "blur": 0,
      "color": {
        "value": "#000000"
      },
      "enable": false,
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "shape": {
      "options": {},
      "type": "circle"
    },
    "size": {
      "random": {
        "enable": true,
        "minimumValue": 1
      },
      "value": 3,
      "animation": {
        "destroy": "none",
        "enable": true,
        "minimumValue": 1,
        "speed": 3,
        "startValue": "max",
        "sync": false
      }
    },
    "stroke": {
      "width": 0,
      "color": {
        "value": "",
        "animation": {
          "enable": false,
          "speed": 0,
          "sync": false
        }
      }
    },
    "twinkle": {
      "lines": {
        "enable": false,
        "frequency": 0.05,
        "opacity": 1
      },
      "particles": {
        "enable": false,
        "frequency": 0.05,
        "opacity": 1
      }
    }
  },
  "pauseOnBlur": true,
  "pauseOnOutsideViewport": false,
  "themes": []
}'
    />
      <div>
        <v-row justify="center">
          <v-col
            cols="12"
            sm="8"
          >
            <v-card max-width="800" class="mx-auto">
              <v-card-title class="blue darken-1">
                <span class="headline white--text">Fashion Shopping Helper</span>
                <v-spacer></v-spacer>
                <v-tooltip right>
                  <template v-slot:activator="{ on, attrs }">
                    <div v-bind="attrs" v-on="on"><v-btn :disabled="submitBtnDisabled" @click="uploadFile">Upload</v-btn></div>
                  </template>
                  <span v-if="submitBtnDisabled">Please choose a picture</span>
                  <span v-else>Upload picture</span>
                </v-tooltip>
              </v-card-title>
              <div>
                <VueFileAgent
                  v-model="files"
                  :multiple="false"
                  :deletable="true"
                  helpText="Drop image here or browse"
                  @delete="fileDeleted"
                  @select="fileSelected"
                ></VueFileAgent>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueFileAgent from 'vue-file-agent'
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import VueFileAgentStyles from 'vue-file-agent/dist/vue-file-agent.css'

Vue.use(VueFileAgent)

export default {
  name: 'home',
  components: {
  },
  methods: {
    changeTheme () {
      this.isDark = !this.isDark
      this.particlesKey += 1
    },
    openSource () {
      window.open('https://github.com/joeyzhou98/codejam2020', '_blank')
    },
    initParticles () {
      window.particlesJS('particles-js', {})
    },
    uploadFile () {
      let formData = new FormData()
      console.log(this.files)
      console.log(this.files[0])
      formData.append('file', this.files[0].file)
      axios.post('api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      ).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    },
    fileDeleted () {
      this.files = []
      this.submitBtnDisabled = true
    },
    fileSelected () {
      this.submitBtnDisabled = false
    }
  },
  data: function () {
    return {
      uploadUrl: 'https://example.com',
      isDark: true,
      files: [],
      submitBtnDisabled: true,
      particlesKey: 0
    }
  },
  mounted () {
    this.initParticles()
  }
}
</script>

<style>
#tsparticles {
  height: 100%;
  width: 100%;
  position: absolute;
}
</style>
