from django.db import models
from django.core.cache import cache
from django.core.validators import MaxValueValidator, MinValueValidator

from boranga import settings


class GeoserverUrl(models.Model):
    url = models.CharField(max_length=255, unique=True)
    wms_version = models.CharField(max_length=10, default="1.3.0")

    class Meta:
        app_label = "boranga"
        ordering = ["url"]
        verbose_name = "Geoserver URL"
        verbose_name_plural = "Geoserver URLs"

    def __str__(self):
        return self.url

    @property
    def get_capabilities_url(self):
        return f"{self.url}/?SERVICE=WMS&VERSION={self.wms_version}&REQUEST=GetCapabilities"


class TileLayer(models.Model):
    geoserver_url = models.ForeignKey(
        GeoserverUrl, on_delete=models.CASCADE, null=False, blank=False
    )
    layer_name = models.CharField(
        max_length=255, unique=True, null=False, blank=False
    )  # Name of the layer in Geoserver
    layer_title = models.CharField(max_length=255)  # Title of the layer
    display_title = models.CharField(
        max_length=255
    )  # Title to display in the layer switcher
    is_satellite_background = models.BooleanField(
        default=False
    )  # Whether the layer is the satellite background layer (mutually exclusive with is_streets_background)
    is_streets_background = models.BooleanField(
        default=False
    )  # Whether the layer is the streets background layer (mutually exclusive with is_satellite_background)
    is_external = models.BooleanField(
        default=True
    )  # Whether the layer is available for external use
    is_internal = models.BooleanField(
        default=True
    )  # Whether the layer is available for internal use
    visible = models.BooleanField(
        default=False
    )  # Whether the layer is visible by default
    active = models.BooleanField(
        default=True
    )  # Whether the layer is disabled and won't be used by the map component
    min_zoom = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(21)],
        null=False,
        blank=False,
    )  # Minimum zoom level at which the layer is visible
    max_zoom = models.PositiveIntegerField(
        default=21,
        validators=[MinValueValidator(0), MaxValueValidator(21)],
        null=False,
        blank=False,
    )  # Maximum zoom level at which the layer is visible
    is_tenure_intersects_query_layer = models.BooleanField(
        default=False
    )  # Whether the layer is used for querying tenure intersects
    invert_xy = models.BooleanField(
        default=False
    )  # Whether the x and y coordinates should be inverted

    class Meta:
        app_label = "boranga"
        ordering = ["display_title", "layer_name"]
        verbose_name = "Geoserver Tile Layer"
        verbose_name_plural = "Geoserver Tile Layers"
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    ~models.Q(
                        ("is_satellite_background", True),
                        ("is_streets_background", True),
                    ),
                ),
                name="tilelayer_is_either_satellite_or_streets_background_or_neither",
            ),
        ]

    def __str__(self):
        return self.layer_name

    def save(self, *args, **kwargs):
        # Clear the cache for the proxy layer data
        cache_key = settings.CACHE_KEY_PROXY_LAYER_DATA.format(
            app_label="boranga", model_name="tilelayer"
        )
        cache.delete(cache_key)

        super().save(*args, **kwargs)


class Proxy(models.Model):
    request_path = models.CharField(max_length=255)
    proxy_url = models.CharField(max_length=255)
    basic_auth_enabled = models.BooleanField(default=False)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = "boranga"
        ordering = ["request_path"]
        verbose_name = "Proxy"
        verbose_name_plural = "Proxies"

    def save(self, *args, **kwargs):
        if self.basic_auth_enabled:
            if self.username == "" or self.password == "":
                raise ValueError("Username and password are required for basic auth")

        # Clear the cache for the proxy data
        cache_key = settings.CACHE_KEY_PROXY_NODE_DATA.format(
            request_path=self.request_path
        )
        cache.delete(cache_key)
        super().save(*args, **kwargs)
