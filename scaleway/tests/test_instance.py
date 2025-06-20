import unittest
import uuid
import time

from scaleway_core.client import Client
from scaleway.scaleway.instance.v1.api import InstanceV1API
from scaleway.scaleway.instance.v1.types import VolumeServerTemplate

class TestE2EServerCreation(unittest.TestCase):
    def setUp(self) -> None:
        self.zone = "fr-par-1"
        self.client = Client() 
        self.api = InstanceV1API(self.client, bypass_validation=True)

    def test_create_and_delete_server(self):
        types = self.api.list_servers_types(zone=self.zone)
        self.assertGreater(types.total_count, 0, "No server types available")
        commercial_type = next(iter(types.server_types))

        images = self.api.list_images(zone=self.zone)
        image_id = None
        for img in images.images:
            if img.arch == "x86_64" and img.root_volume:
                image_id = img.id
                break
        self.assertIsNotNone(image_id, "No suitable image found")

        server_name = f"test-{uuid.uuid4().hex[:6]}"
        volume = {"0": VolumeServerTemplate(size=20 * 1024 ** 3)} 

        server = self.api._create_server(
            commercial_type=commercial_type,
            zone=self.zone,
            name=server_name,
            image=image_id,
            dynamic_ip_required=True,
            volumes=volume,
        )

        self.assertEqual(server.name, server_name)
        self.assertEqual(server.image.id, image_id)
        self.assertIsNotNone(server.id)
        print(f"✅ Created server: {server.id}")

        for _ in range(10):
            s = self.api.get_server(zone=self.zone, server_id=server.id)
            if s.state == "running":
                print(f"✅ Server {server.id} is running.")
                break
            time.sleep(5)
        else:
            self.fail("Server did not reach 'running' state in time.")

        self.api.delete_server(zone=self.zone, server_id=server.id)
        print(f"🗑️ Deleted server: {server.id}")
